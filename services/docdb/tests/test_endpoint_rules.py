
import pytest
from aws_sdk_docdb._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_docdb._rule_engine._endpoint_runtime import EndpointError
import re
import zapros


def test_1_for_region_af_south_1_with_fips_disabled():
    """For region af-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='af-south-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.af-south-1.amazonaws.com'


def test_2_for_region_ap_east_1_with_fips_disabled_():
    """For region ap-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='ap-east-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.ap-east-1.amazonaws.com'


def test_3_for_region_ap_northeast_1_with_fips_disa():
    """For region ap-northeast-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='ap-northeast-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.ap-northeast-1.amazonaws.com'


def test_4_for_region_ap_northeast_2_with_fips_disa():
    """For region ap-northeast-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='ap-northeast-2',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.ap-northeast-2.amazonaws.com'


def test_5_for_region_ap_northeast_3_with_fips_disa():
    """For region ap-northeast-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='ap-northeast-3',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.ap-northeast-3.amazonaws.com'


def test_6_for_region_ap_south_1_with_fips_disabled():
    """For region ap-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='ap-south-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.ap-south-1.amazonaws.com'


def test_7_for_region_ap_southeast_1_with_fips_disa():
    """For region ap-southeast-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='ap-southeast-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.ap-southeast-1.amazonaws.com'


def test_8_for_region_ap_southeast_2_with_fips_disa():
    """For region ap-southeast-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='ap-southeast-2',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.ap-southeast-2.amazonaws.com'


def test_9_for_region_ap_southeast_3_with_fips_disa():
    """For region ap-southeast-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='ap-southeast-3',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.ap-southeast-3.amazonaws.com'


def test_10_for_region_ca_central_1_with_fips_disabl():
    """For region ca-central-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='ca-central-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.ca-central-1.amazonaws.com'


def test_11_for_region_ca_central_1_with_fips_enable():
    """For region ca-central-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(
        Region='ca-central-1',
        UseFIPS=True,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds-fips.ca-central-1.amazonaws.com'


def test_12_for_region_eu_central_1_with_fips_disabl():
    """For region eu-central-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='eu-central-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.eu-central-1.amazonaws.com'


def test_13_for_region_eu_north_1_with_fips_disabled():
    """For region eu-north-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='eu-north-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.eu-north-1.amazonaws.com'


def test_14_for_region_eu_south_1_with_fips_disabled():
    """For region eu-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='eu-south-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.eu-south-1.amazonaws.com'


def test_15_for_region_eu_west_1_with_fips_disabled_():
    """For region eu-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='eu-west-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.eu-west-1.amazonaws.com'


def test_16_for_region_eu_west_2_with_fips_disabled_():
    """For region eu-west-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='eu-west-2',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.eu-west-2.amazonaws.com'


def test_17_for_region_eu_west_3_with_fips_disabled_():
    """For region eu-west-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='eu-west-3',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.eu-west-3.amazonaws.com'


def test_18_for_region_me_south_1_with_fips_disabled():
    """For region me-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='me-south-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.me-south-1.amazonaws.com'


def test_19_for_region_sa_east_1_with_fips_disabled_():
    """For region sa-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='sa-east-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.sa-east-1.amazonaws.com'


def test_20_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='us-east-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.us-east-1.amazonaws.com'


def test_21_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(
        Region='us-east-1',
        UseFIPS=True,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds-fips.us-east-1.amazonaws.com'


def test_22_for_region_us_east_2_with_fips_disabled_():
    """For region us-east-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='us-east-2',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.us-east-2.amazonaws.com'


def test_23_for_region_us_east_2_with_fips_enabled_a():
    """For region us-east-2 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(
        Region='us-east-2',
        UseFIPS=True,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds-fips.us-east-2.amazonaws.com'


def test_24_for_region_us_west_1_with_fips_disabled_():
    """For region us-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='us-west-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.us-west-1.amazonaws.com'


def test_25_for_region_us_west_1_with_fips_enabled_a():
    """For region us-west-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(
        Region='us-west-1',
        UseFIPS=True,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds-fips.us-west-1.amazonaws.com'


def test_26_for_region_us_west_2_with_fips_disabled_():
    """For region us-west-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='us-west-2',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.us-west-2.amazonaws.com'


def test_27_for_region_us_west_2_with_fips_enabled_a():
    """For region us-west-2 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(
        Region='us-west-2',
        UseFIPS=True,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds-fips.us-west-2.amazonaws.com'


def test_28_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(
        Region='us-east-1',
        UseFIPS=True,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://rds-fips.us-east-1.api.aws'


def test_29_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(
        Region='us-east-1',
        UseFIPS=False,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://rds.us-east-1.api.aws'


def test_30_for_region_cn_north_1_with_fips_disabled():
    """For region cn-north-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='cn-north-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.cn-north-1.amazonaws.com.cn'


def test_31_for_region_cn_northwest_1_with_fips_disa():
    """For region cn-northwest-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='cn-northwest-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.cn-northwest-1.amazonaws.com.cn'


def test_32_for_region_cn_north_1_with_fips_enabled_():
    """For region cn-north-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(
        Region='cn-north-1',
        UseFIPS=True,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://rds-fips.cn-north-1.api.amazonwebservices.com.cn'


def test_33_for_region_cn_north_1_with_fips_enabled_():
    """For region cn-north-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(
        Region='cn-north-1',
        UseFIPS=True,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds-fips.cn-north-1.amazonaws.com.cn'


def test_34_for_region_cn_north_1_with_fips_disabled():
    """For region cn-north-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(
        Region='cn-north-1',
        UseFIPS=False,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://rds.cn-north-1.api.amazonwebservices.com.cn'


def test_35_for_region_us_gov_east_1_with_fips_disab():
    """For region us-gov-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='us-gov-east-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.us-gov-east-1.amazonaws.com'


def test_36_for_region_us_gov_east_1_with_fips_enabl():
    """For region us-gov-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(
        Region='us-gov-east-1',
        UseFIPS=True,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.us-gov-east-1.amazonaws.com'


def test_37_for_region_us_gov_west_1_with_fips_disab():
    """For region us-gov-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='us-gov-west-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.us-gov-west-1.amazonaws.com'


def test_38_for_region_us_gov_west_1_with_fips_enabl():
    """For region us-gov-west-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(
        Region='us-gov-west-1',
        UseFIPS=True,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.us-gov-west-1.amazonaws.com'


def test_39_for_region_us_gov_east_1_with_fips_enabl():
    """For region us-gov-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(
        Region='us-gov-east-1',
        UseFIPS=True,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://rds-fips.us-gov-east-1.api.aws'


def test_40_for_region_us_gov_east_1_with_fips_disab():
    """For region us-gov-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(
        Region='us-gov-east-1',
        UseFIPS=False,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://rds.us-gov-east-1.api.aws'


def test_41_for_region_us_iso_east_1_with_fips_disab():
    """For region us-iso-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='us-iso-east-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.us-iso-east-1.c2s.ic.gov'


def test_42_for_region_us_iso_west_1_with_fips_disab():
    """For region us-iso-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='us-iso-west-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.us-iso-west-1.c2s.ic.gov'


def test_43_for_region_us_iso_east_1_with_fips_enabl():
    """For region us-iso-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(
        Region='us-iso-east-1',
        UseFIPS=True,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds-fips.us-iso-east-1.c2s.ic.gov'


def test_44_for_region_us_isob_east_1_with_fips_disa():
    """For region us-isob-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(
        Region='us-isob-east-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds.us-isob-east-1.sc2s.sgov.gov'


def test_45_for_region_us_isob_east_1_with_fips_enab():
    """For region us-isob-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(
        Region='us-isob-east-1',
        UseFIPS=True,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://rds-fips.us-isob-east-1.sc2s.sgov.gov'


def test_46_for_custom_endpoint_with_region_set_and_():
    """For custom endpoint with region set and fips disabled and dualstack disabled"""
    params = EndpointParams(
        Region='us-east-1',
        UseFIPS=False,
        UseDualStack=False,
        Endpoint='https://example.com',
    )

    result = resolve(params)
    assert result.url == 'https://example.com'


def test_47_for_custom_endpoint_with_region_not_set_():
    """For custom endpoint with region not set and fips disabled and dualstack disabled"""
    params = EndpointParams(
        UseFIPS=False,
        UseDualStack=False,
        Endpoint='https://example.com',
    )

    result = resolve(params)
    assert result.url == 'https://example.com'


def test_48_for_custom_endpoint_with_fips_enabled_an():
    """For custom endpoint with fips enabled and dualstack disabled"""
    params = EndpointParams(
        Region='us-east-1',
        UseFIPS=True,
        UseDualStack=False,
        Endpoint='https://example.com',
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)


def test_49_for_custom_endpoint_with_fips_disabled_a():
    """For custom endpoint with fips disabled and dualstack enabled"""
    params = EndpointParams(
        Region='us-east-1',
        UseFIPS=False,
        UseDualStack=True,
        Endpoint='https://example.com',
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)


def test_50_missing_region():
    """Missing region"""
    params = EndpointParams(
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Missing Region')):
        resolve(params)


