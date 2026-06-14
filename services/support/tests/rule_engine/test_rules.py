import pytest
from aws_sdk_support._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_support._rule_engine._endpoint_runtime import EndpointError
import re
import zapros

def test_1_for_region_aws_global_with_fips_disabled():
    """For region aws-global with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='aws-global', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://support.us-east-1.amazonaws.com'

def test_2_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://support-fips.us-east-1.api.aws'

def test_3_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://support-fips.us-east-1.amazonaws.com'

def test_4_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://support.us-east-1.api.aws'

def test_5_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://support.us-east-1.amazonaws.com'

def test_6_for_region_aws_cn_global_with_fips_disab():
    """For region aws-cn-global with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='aws-cn-global', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://support.cn-north-1.amazonaws.com.cn'

def test_7_for_region_cn_north_1_with_fips_enabled_():
    """For region cn-north-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://support-fips.cn-north-1.api.amazonwebservices.com.cn'

def test_8_for_region_cn_north_1_with_fips_enabled_():
    """For region cn-north-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://support-fips.cn-north-1.amazonaws.com.cn'

def test_9_for_region_cn_north_1_with_fips_disabled():
    """For region cn-north-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://support.cn-north-1.api.amazonwebservices.com.cn'

def test_10_for_region_cn_north_1_with_fips_disabled():
    """For region cn-north-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://support.cn-north-1.amazonaws.com.cn'

def test_11_for_region_aws_us_gov_global_with_fips_d():
    """For region aws-us-gov-global with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='aws-us-gov-global', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://support.us-gov-west-1.amazonaws.com'

def test_12_for_region_aws_us_gov_global_with_fips_e():
    """For region aws-us-gov-global with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='aws-us-gov-global', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://support.us-gov-west-1.amazonaws.com'

def test_13_for_region_us_gov_east_1_with_fips_enabl():
    """For region us-gov-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://support-fips.us-gov-east-1.api.aws'

def test_14_for_region_us_gov_east_1_with_fips_enabl():
    """For region us-gov-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://support.us-gov-west-1.amazonaws.com'

def test_15_for_region_us_gov_east_1_with_fips_disab():
    """For region us-gov-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://support.us-gov-east-1.api.aws'

def test_16_for_region_us_gov_east_1_with_fips_disab():
    """For region us-gov-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://support.us-gov-west-1.amazonaws.com'

def test_17_for_region_aws_iso_global_with_fips_disa():
    """For region aws-iso-global with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='aws-iso-global', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://support.us-iso-east-1.c2s.ic.gov'

def test_18_for_region_us_iso_east_1_with_fips_enabl():
    """For region us-iso-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://support-fips.us-iso-east-1.c2s.ic.gov'

def test_19_for_region_us_iso_east_1_with_fips_disab():
    """For region us-iso-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://support.us-iso-east-1.c2s.ic.gov'

def test_20_for_region_aws_iso_b_global_with_fips_di():
    """For region aws-iso-b-global with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='aws-iso-b-global', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://support.us-isob-east-1.sc2s.sgov.gov'

def test_21_for_region_us_isob_east_1_with_fips_enab():
    """For region us-isob-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://support-fips.us-isob-east-1.sc2s.sgov.gov'

def test_22_for_region_us_isob_east_1_with_fips_disa():
    """For region us-isob-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://support.us-isob-east-1.sc2s.sgov.gov'

def test_23_for_custom_endpoint_with_region_set_and_():
    """For custom endpoint with region set and fips disabled and dualstack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_24_for_custom_endpoint_with_region_not_set_():
    """For custom endpoint with region not set and fips disabled and dualstack disabled"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_25_for_custom_endpoint_with_fips_enabled_an():
    """For custom endpoint with fips enabled and dualstack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_26_for_custom_endpoint_with_fips_disabled_a():
    """For custom endpoint with fips disabled and dualstack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test_27_missing_region():
    """Missing region"""
    params = EndpointParams()
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Missing Region')):
        resolve(params)