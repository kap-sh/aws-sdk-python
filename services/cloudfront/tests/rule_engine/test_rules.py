import pytest
from aws_sdk_cloudfront._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_cloudfront._rule_engine._endpoint_runtime import EndpointError
import re
import zapros

def test_for_custom_endpoint_with_region_not_set_():
    """For custom endpoint with region not set and fips disabled"""
    params = EndpointParams(Endpoint='https://example.com', UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_for_custom_endpoint_with_fips_enabled():
    """For custom endpoint with fips enabled"""
    params = EndpointParams(Endpoint='https://example.com', UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_for_custom_endpoint_with_fips_disabled_a():
    """For custom endpoint with fips disabled and dualstack enabled"""
    params = EndpointParams(Endpoint='https://example.com', UseFIPS=False, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://cloudfront-fips.global.api.aws'

def test_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://cloudfront-fips.amazonaws.com'

def test_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://cloudfront.global.api.aws'

def test_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://cloudfront.amazonaws.com'

def test_for_region_cn_northwest_1_with_fips_enab():
    """For region cn-northwest-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://cloudfront-fips.api.amazonwebservices.com.cn'

def test_for_region_cn_northwest_1_with_fips_enab():
    """For region cn-northwest-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://cloudfront-fips.cn-northwest-1.amazonaws.com.cn'

def test_for_region_cn_northwest_1_with_fips_disa():
    """For region cn-northwest-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://cloudfront.api.amazonwebservices.com.cn'

def test_for_region_cn_northwest_1_with_fips_disa():
    """For region cn-northwest-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://cloudfront.cn-northwest-1.amazonaws.com.cn'

def test_for_region_eusc_de_east_1_with_fips_enab():
    """For region eusc-de-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='eusc-de-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://cloudfront-fips.amazonaws.eu'

def test_for_region_eusc_de_east_1_with_fips_disa():
    """For region eusc-de-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eusc-de-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://cloudfront.amazonaws.eu'

def test_for_region_us_iso_east_1_with_fips_enabl():
    """For region us-iso-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://cloudfront-fips.c2s.ic.gov'

def test_for_region_us_iso_east_1_with_fips_disab():
    """For region us-iso-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://cloudfront.c2s.ic.gov'

def test_for_region_us_isob_east_1_with_fips_enab():
    """For region us-isob-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://cloudfront-fips.sc2s.sgov.gov'

def test_for_region_us_isob_east_1_with_fips_disa():
    """For region us-isob-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://cloudfront.sc2s.sgov.gov'

def test_for_region_eu_isoe_west_1_with_fips_enab():
    """For region eu-isoe-west-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='eu-isoe-west-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://cloudfront-fips.cloud.adc-e.uk'

def test_for_region_eu_isoe_west_1_with_fips_disa():
    """For region eu-isoe-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-isoe-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://cloudfront.cloud.adc-e.uk'

def test_for_region_us_isof_south_1_with_fips_ena():
    """For region us-isof-south-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-isof-south-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://cloudfront-fips.csp.hci.ic.gov'

def test_for_region_us_isof_south_1_with_fips_dis():
    """For region us-isof-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-isof-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://cloudfront.csp.hci.ic.gov'

def test_for_region_us_gov_west_1_with_fips_enabl():
    """For region us-gov-west-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://cloudfront-fips.api.aws'

def test_for_region_us_gov_west_1_with_fips_enabl():
    """For region us-gov-west-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://cloudfront-fips.amazonaws.com'

def test_for_region_us_gov_west_1_with_fips_disab():
    """For region us-gov-west-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://cloudfront.api.aws'

def test_for_region_us_gov_west_1_with_fips_disab():
    """For region us-gov-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://cloudfront.amazonaws.com'

def test_missing_region():
    """Missing region"""
    params = EndpointParams()
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Missing Region')):
        resolve(params)