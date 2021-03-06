import milksets.wine
import milksets.yeast
import milksets.german

def test_classification_loaders():
    def test_loader(module):
        features,labels = module.load()
        assert len(features) == len(labels)
        assert labels.min() == 0
        assert labels.max() == len(module.label_names) - 1
        assert (features.std(0)**2).sum() > 1e-8
    yield test_loader, milksets.wine
    yield test_loader, milksets.yeast
    yield test_loader, milksets.murphy_hela_slf7dna
    yield test_loader, milksets.german

