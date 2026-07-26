import pytest
from capo_kinesis._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_kinesis._rule_engine._endpoint_runtime import EndpointError
import re
import zapros

def test_for_region_af_south_1_with_fips_disabled():
    """For region af-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='af-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.af-south-1.amazonaws.com'

def test_for_region_ap_east_1_with_fips_disabled_():
    """For region ap-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.ap-east-1.amazonaws.com'

def test_for_region_ap_northeast_1_with_fips_disa():
    """For region ap-northeast-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.ap-northeast-1.amazonaws.com'

def test_for_region_ap_northeast_2_with_fips_disa():
    """For region ap-northeast-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.ap-northeast-2.amazonaws.com'

def test_for_region_ap_northeast_3_with_fips_disa():
    """For region ap-northeast-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-3', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.ap-northeast-3.amazonaws.com'

def test_for_region_ap_south_1_with_fips_disabled():
    """For region ap-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.ap-south-1.amazonaws.com'

def test_for_region_ap_southeast_1_with_fips_disa():
    """For region ap-southeast-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.ap-southeast-1.amazonaws.com'

def test_for_region_ap_southeast_2_with_fips_disa():
    """For region ap-southeast-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.ap-southeast-2.amazonaws.com'

def test_for_region_ap_southeast_3_with_fips_disa():
    """For region ap-southeast-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-3', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.ap-southeast-3.amazonaws.com'

def test_for_region_ca_central_1_with_fips_disabl():
    """For region ca-central-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ca-central-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.ca-central-1.amazonaws.com'

def test_for_region_eu_central_1_with_fips_disabl():
    """For region eu-central-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-central-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.eu-central-1.amazonaws.com'

def test_for_region_eu_north_1_with_fips_disabled():
    """For region eu-north-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-north-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.eu-north-1.amazonaws.com'

def test_for_region_eu_south_1_with_fips_disabled():
    """For region eu-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.eu-south-1.amazonaws.com'

def test_for_region_eu_west_1_with_fips_disabled_():
    """For region eu-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.eu-west-1.amazonaws.com'

def test_for_region_eu_west_2_with_fips_disabled_():
    """For region eu-west-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.eu-west-2.amazonaws.com'

def test_for_region_eu_west_3_with_fips_disabled_():
    """For region eu-west-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-3', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.eu-west-3.amazonaws.com'

def test_for_region_me_south_1_with_fips_disabled():
    """For region me-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='me-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.me-south-1.amazonaws.com'

def test_for_region_sa_east_1_with_fips_disabled_():
    """For region sa-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='sa-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.sa-east-1.amazonaws.com'

def test_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-east-1.amazonaws.com'

def test_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-east-1.amazonaws.com'

def test_for_region_us_east_2_with_fips_disabled_():
    """For region us-east-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-east-2.amazonaws.com'

def test_for_region_us_east_2_with_fips_enabled_a():
    """For region us-east-2 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-2', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-east-2.amazonaws.com'

def test_for_region_us_west_1_with_fips_disabled_():
    """For region us-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-west-1.amazonaws.com'

def test_for_region_us_west_1_with_fips_enabled_a():
    """For region us-west-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-west-1.amazonaws.com'

def test_for_region_us_west_2_with_fips_disabled_():
    """For region us-west-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-west-2.amazonaws.com'

def test_for_region_us_west_2_with_fips_enabled_a():
    """For region us-west-2 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-2', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-west-2.amazonaws.com'

def test_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-east-1.api.aws'

def test_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-east-1.api.aws'

def test_for_region_cn_north_1_with_fips_disabled():
    """For region cn-north-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.cn-north-1.amazonaws.com.cn'

def test_for_region_cn_northwest_1_with_fips_disa():
    """For region cn-northwest-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.cn-northwest-1.amazonaws.com.cn'

def test_for_region_cn_north_1_with_fips_enabled_():
    """For region cn-north-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.cn-north-1.api.amazonwebservices.com.cn'

def test_for_region_cn_north_1_with_fips_enabled_():
    """For region cn-north-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.cn-north-1.amazonaws.com.cn'

def test_for_region_cn_north_1_with_fips_disabled():
    """For region cn-north-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://kinesis.cn-north-1.api.amazonwebservices.com.cn'

def test_for_region_us_gov_east_1_with_fips_disab():
    """For region us-gov-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-gov-east-1.amazonaws.com'

def test_for_region_us_gov_east_1_with_fips_enabl():
    """For region us-gov-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-gov-east-1.amazonaws.com'

def test_for_region_us_gov_west_1_with_fips_disab():
    """For region us-gov-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-gov-west-1.amazonaws.com'

def test_for_region_us_gov_west_1_with_fips_enabl():
    """For region us-gov-west-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-gov-west-1.amazonaws.com'

def test_for_region_us_gov_east_1_with_fips_enabl():
    """For region us-gov-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-gov-east-1.api.aws'

def test_for_region_us_gov_east_1_with_fips_disab():
    """For region us-gov-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-gov-east-1.api.aws'

def test_for_region_us_iso_east_1_with_fips_disab():
    """For region us-iso-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-east-1.c2s.ic.gov'

def test_for_region_us_iso_west_1_with_fips_disab():
    """For region us-iso-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-west-1.c2s.ic.gov'

def test_for_region_us_iso_east_1_with_fips_enabl():
    """For region us-iso-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-iso-east-1.c2s.ic.gov'

def test_for_region_us_isob_east_1_with_fips_disa():
    """For region us-isob-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis.us-isob-east-1.sc2s.sgov.gov'

def test_for_region_us_isob_east_1_with_fips_enab():
    """For region us-isob-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-isob-east-1.sc2s.sgov.gov'

def test_for_custom_endpoint_with_region_set_and_():
    """For custom endpoint with region set and fips disabled and dualstack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_for_custom_endpoint_with_region_not_set_():
    """For custom endpoint with region not set and fips disabled and dualstack disabled"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_for_custom_endpoint_with_fips_enabled_an():
    """For custom endpoint with fips enabled and dualstack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_for_custom_endpoint_with_fips_disabled_a():
    """For custom endpoint with fips disabled and dualstack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test_missing_region():
    """Missing region"""
    params = EndpointParams()
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Missing Region')):
        resolve(params)

def test_invalid_arn__failed_to_parse_arn_():
    """Invalid ARN: Failed to parse ARN."""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, StreamARN='arn')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Failed to parse ARN.')):
        resolve(params)

def test_invalid_arn__partition_missing_from_arn_():
    """Invalid ARN: partition missing from ARN."""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, StreamARN='arn::kinesis:us-west-2:123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Failed to parse ARN.')):
        resolve(params)

def test_invalid_arn__partitions_mismatch_():
    """Invalid ARN: partitions mismatch."""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=False, StreamARN='arn:aws:kinesis:us-west-2:123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape("Partition: aws from ARN doesn't match with partition name: aws-us-gov.")):
        resolve(params)

def test_invalid_arn__not_kinesis():
    """Invalid ARN: Not Kinesis"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, StreamARN='arn:aws:s3:us-west-2:123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The ARN was not for the Kinesis service, found: s3.')):
        resolve(params)

def test_invalid_arn__region_is_missing_in_arn():
    """Invalid ARN: Region is missing in ARN"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, StreamARN='arn:aws:kinesis::123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid region.')):
        resolve(params)

def test_invalid_arn__region_is_empty_string_in_a():
    """Invalid ARN: Region is empty string in ARN"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, StreamARN='arn:aws:kinesis:  :123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid region.')):
        resolve(params)

def test_invalid_arn__invalid_account_id():
    """Invalid ARN: Invalid account id"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, StreamARN='arn:aws:kinesis:us-east-1::stream/testStream', OperationType='control')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid account id.')):
        resolve(params)

def test_invalid_arn__invalid_account_id():
    """Invalid ARN: Invalid account id"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, StreamARN='arn:aws:kinesis:us-east-1:   :stream/testStream', OperationType='control')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid account id.')):
        resolve(params)

def test_invalid_arn__kinesis_arns_only_support_s():
    """Invalid ARN: Kinesis ARNs only support stream arn types"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, StreamARN='arn:aws:kinesis:us-east-1:123:accesspoint/testStream')
    with pytest.raises(EndpointError, match=re.escape("Invalid ARN: Kinesis ARNs don't support `accesspoint` arn types.")):
        resolve(params)

def test_operationtype_not_set():
    """OperationType not set"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, StreamARN='arn:aws:kinesis:us-east-1:123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape('Operation Type is not set. Please contact service team for resolution.')):
        resolve(params)

def test_custom_endpoint_is_specified():
    """Custom Endpoint is specified"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_account_endpoint_targeting_control_opera():
    """Account endpoint targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-east-1.amazonaws.com'

def test_account_endpoint_targeting_data_operatio():
    """Account endpoint targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-east-1.amazonaws.com'

def test_account_endpoint_with_fips_targeting_dat():
    """Account endpoint with fips targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.us-east-1.amazonaws.com'

def test_account_endpoint_with_fips_targeting_con():
    """Account endpoint with fips targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis-fips.us-east-1.amazonaws.com'

def test_account_endpoint_with_dual_stack_and_fip():
    """Account endpoint with Dual Stack and FIPS enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis-fips.us-east-1.api.aws'

def test_account_endpoint_with_dual_stack_enabled():
    """Account endpoint with Dual Stack enabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=True, OperationType='data', StreamARN='arn:aws:kinesis:us-west-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-west-1.api.aws'

def test_account_endpoint_with_fips_and_dualstack():
    """Account endpoint with FIPS and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=False, OperationType='control', StreamARN='arn:aws:kinesis:us-west-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-west-1.amazonaws.com'

def test_regionmismatch__client_region_should_be_():
    """RegionMismatch: client region should be used for endpoint region"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', StreamARN='arn:aws:kinesis:us-west-1:123:stream/testStream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-east-1.amazonaws.com'

def test_account_endpoint_with_fips_enabled():
    """Account endpoint with FIPS enabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=False, OperationType='data', StreamARN='arn:aws-cn:kinesis:cn-northwest-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.cn-northwest-1.amazonaws.com.cn'

def test_account_endpoint_with_fips_and_dualstack():
    """Account endpoint with FIPS and DualStack enabled for cn regions."""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=True, OperationType='data', StreamARN='arn:aws-cn:kinesis:cn-northwest-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.cn-northwest-1.api.amazonwebservices.com.cn'

def test_account_endpoint_targeting_control_opera():
    """Account endpoint targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', StreamARN='arn:aws-iso:kinesis:us-iso-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-east-1.c2s.ic.gov'

def test_account_endpoint_targeting_control_opera():
    """Account endpoint targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-west-1', UseFIPS=False, UseDualStack=False, OperationType='control', StreamARN='arn:aws-iso:kinesis:us-iso-west-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-west-1.c2s.ic.gov'

def test_account_endpoint_targeting_data_operatio():
    """Account endpoint targeting data operation type in ADC regions"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', StreamARN='arn:aws-iso-b:kinesis:us-isob-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-isob-east-1.sc2s.sgov.gov'

def test_account_endpoint_with_fips_targeting_con():
    """Account endpoint with fips targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', StreamARN='arn:aws-iso:kinesis:us-iso-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-iso-east-1.c2s.ic.gov'

def test_account_endpoint_with_fips_targeting_dat():
    """Account endpoint with fips targeting data operation type in ADC regions"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', StreamARN='arn:aws-iso-b:kinesis:us-isob-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-isob-east-1.sc2s.sgov.gov'

def test_invalid_consumerarn__failed_to_parse_arn():
    """Invalid ConsumerARN: Failed to parse ARN."""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ConsumerARN='arn')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Failed to parse ARN.')):
        resolve(params)

def test_invalid_consumerarn__partition_missing_f():
    """Invalid ConsumerARN: partition missing from ARN."""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ConsumerARN='arn::kinesis:us-west-2:123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Failed to parse ARN.')):
        resolve(params)

def test_invalid_arn__partitions_mismatch_():
    """Invalid ARN: partitions mismatch."""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=False, ConsumerARN='arn:aws:kinesis:us-west-2:123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape("Partition: aws from ARN doesn't match with partition name: aws-us-gov.")):
        resolve(params)

def test_invalid_arn__not_kinesis():
    """Invalid ARN: Not Kinesis"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ConsumerARN='arn:aws:s3:us-west-2:123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The ARN was not for the Kinesis service, found: s3.')):
        resolve(params)

def test_invalid_arn__region_is_missing_in_arn():
    """Invalid ARN: Region is missing in ARN"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ConsumerARN='arn:aws:kinesis::123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid region.')):
        resolve(params)

def test_invalid_arn__region_is_empty_string_in_a():
    """Invalid ARN: Region is empty string in ARN"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ConsumerARN='arn:aws:kinesis:  :123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid region.')):
        resolve(params)

def test_invalid_arn__invalid_account_id():
    """Invalid ARN: Invalid account id"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ConsumerARN='arn:aws:kinesis:us-east-1::stream/testStream/consumer/test-consumer:1525898737', OperationType='control')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid account id.')):
        resolve(params)

def test_invalid_arn__invalid_account_id():
    """Invalid ARN: Invalid account id"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ConsumerARN='arn:aws:kinesis:us-east-1:   :stream/testStream/consumer/test-consumer:1525898737', OperationType='control')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid account id.')):
        resolve(params)

def test_invalid_arn__kinesis_arns_only_support_s():
    """Invalid ARN: Kinesis ARNs only support stream arn/consumer arn types"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ConsumerARN='arn:aws:kinesis:us-east-1:123:accesspoint/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape("Invalid ARN: Kinesis ARNs don't support `accesspoint` arn types.")):
        resolve(params)

def test_operationtype_not_set():
    """OperationType not set"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ConsumerARN='arn:aws:kinesis:us-east-1:123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape('Operation Type is not set. Please contact service team for resolution.')):
        resolve(params)

def test_custom_endpoint_is_specified():
    """Custom Endpoint is specified"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ConsumerARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_account_endpoint_targeting_control_opera():
    """Account endpoint targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ConsumerARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-east-1.amazonaws.com'

def test_account_endpoint_targeting_data_operatio():
    """Account endpoint targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ConsumerARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-east-1.amazonaws.com'

def test_account_endpoint_with_fips_targeting_dat():
    """Account endpoint with fips targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', ConsumerARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.us-east-1.amazonaws.com'

def test_account_endpoint_with_fips_targeting_con():
    """Account endpoint with fips targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', ConsumerARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis-fips.us-east-1.amazonaws.com'

def test_account_endpoint_with_dual_stack_and_fip():
    """Account endpoint with Dual Stack and FIPS enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', ConsumerARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis-fips.us-east-1.api.aws'

def test_account_endpoint_with_dual_stack_enabled():
    """Account endpoint with Dual Stack enabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=True, OperationType='data', ConsumerARN='arn:aws:kinesis:us-west-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-west-1.api.aws'

def test_account_endpoint_with_fips_and_dualstack():
    """Account endpoint with FIPS and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=False, OperationType='control', ConsumerARN='arn:aws:kinesis:us-west-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-west-1.amazonaws.com'

def test_regionmismatch__client_region_should_be_():
    """RegionMismatch: client region should be used for endpoint region"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ConsumerARN='arn:aws:kinesis:us-west-1:123:stream/testStream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-east-1.amazonaws.com'

def test_account_endpoint_with_fips_enabled():
    """Account endpoint with FIPS enabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=False, OperationType='data', ConsumerARN='arn:aws-cn:kinesis:cn-northwest-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.cn-northwest-1.amazonaws.com.cn'

def test_account_endpoint_with_fips_and_dualstack():
    """Account endpoint with FIPS and DualStack enabled for cn regions."""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=True, OperationType='data', ConsumerARN='arn:aws-cn:kinesis:cn-northwest-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.cn-northwest-1.api.amazonwebservices.com.cn'

def test_account_endpoint_targeting_control_opera():
    """Account endpoint targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ConsumerARN='arn:aws-iso:kinesis:us-iso-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-east-1.c2s.ic.gov'

def test_account_endpoint_targeting_control_opera():
    """Account endpoint targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-west-1', UseFIPS=False, UseDualStack=False, OperationType='control', ConsumerARN='arn:aws-iso:kinesis:us-iso-west-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-west-1.c2s.ic.gov'

def test_account_endpoint_targeting_data_operatio():
    """Account endpoint targeting data operation type in ADC regions"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ConsumerARN='arn:aws-iso-b:kinesis:us-isob-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-isob-east-1.sc2s.sgov.gov'

def test_account_endpoint_with_fips_targeting_con():
    """Account endpoint with fips targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', ConsumerARN='arn:aws-iso:kinesis:us-iso-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-iso-east-1.c2s.ic.gov'

def test_account_endpoint_with_fips_targeting_dat():
    """Account endpoint with fips targeting data operation type in ADC regions"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', ConsumerARN='arn:aws-iso-b:kinesis:us-isob-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-isob-east-1.sc2s.sgov.gov'

def test_consumerarn_targeting_us_east_1():
    """ConsumerARN targeting US-EAST-1"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ConsumerARN='arn:aws:kinesis:us-east-1:123456789123:stream/foobar/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123456789123.data-kinesis.us-east-1.amazonaws.com'

def test_both_streamarn_and_consumerarn_specified():
    """Both StreamARN and ConsumerARN specified. StreamARN should take precedence"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', StreamARN='arn:aws:kinesis:us-east-1:123:stream/foobar', ConsumerARN='arn:aws:kinesis:us-east-1:123456789123:stream/foobar/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-east-1.amazonaws.com'

def test_resourcearn_test__invalid_arn__failed_to():
    """ResourceARN test: Invalid ARN: Failed to parse ARN."""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Failed to parse ARN.')):
        resolve(params)

def test_resourcearn_as_streamarn_test__invalid_a():
    """ResourceARN as StreamARN test: Invalid ARN: partition missing from ARN."""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn::kinesis:us-west-2:123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Failed to parse ARN.')):
        resolve(params)

def test_resourcearn_as_streamarn_test__invalid_a():
    """ResourceARN as StreamARN test: Invalid ARN: partitions mismatch."""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:us-west-2:123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape("Partition: aws from ARN doesn't match with partition name: aws-us-gov.")):
        resolve(params)

def test_resourcearn_as_streamarn_test__invalid_a():
    """ResourceARN as StreamARN test: Invalid ARN: Not Kinesis"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:s3:us-west-2:123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The ARN was not for the Kinesis service, found: s3.')):
        resolve(params)

def test_resourcearn_as_streamarn_test__invalid_a():
    """ResourceARN as StreamARN test: Invalid ARN: Region is missing in ARN"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis::123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid region.')):
        resolve(params)

def test_resourcearn_as_streamarn_test__invalid_a():
    """ResourceARN as StreamARN test: Invalid ARN: Region is empty string in ARN"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:  :123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid region.')):
        resolve(params)

def test_resourcearn_as_streamarn_test__invalid_a():
    """ResourceARN as StreamARN test: Invalid ARN: Invalid account id"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:us-east-1::stream/testStream', OperationType='control')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid account id.')):
        resolve(params)

def test_resourcearn_as_streamarn_test__invalid_a():
    """ResourceARN as StreamARN test: Invalid ARN: Invalid account id"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:us-east-1:   :stream/testStream', OperationType='control')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid account id.')):
        resolve(params)

def test_resourcearn_as_streamarn_test__invalid_a():
    """ResourceARN as StreamARN test: Invalid ARN: Kinesis ARNs only support stream arn types"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:us-east-1:123:accesspoint/testStream')
    with pytest.raises(EndpointError, match=re.escape("Invalid ARN: Kinesis ARNs don't support `accesspoint` arn types.")):
        resolve(params)

def test_resourcearn_as_streamarn_test__operation():
    """ResourceARN as StreamARN test: OperationType not set"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:us-east-1:123456789012:stream/testStream')
    with pytest.raises(EndpointError, match=re.escape('Operation Type is not set. Please contact service team for resolution.')):
        resolve(params)

def test_resourcearn_as_streamarn_test__custom_en():
    """ResourceARN as StreamARN test: Custom Endpoint is specified"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-east-1.amazonaws.com'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-east-1.amazonaws.com'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint with fips targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.us-east-1.amazonaws.com'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint with fips targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis-fips.us-east-1.amazonaws.com'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint with Dual Stack and FIPS enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis-fips.us-east-1.api.aws'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint with Dual Stack enabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=True, OperationType='data', ResourceARN='arn:aws:kinesis:us-west-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-west-1.api.aws'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint with FIPS and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-west-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-west-1.amazonaws.com'

def test_resourcearn_as_streamarn_test__regionmis():
    """ResourceARN as StreamARN test: RegionMismatch: client region should be used for endpoint region"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ResourceARN='arn:aws:kinesis:us-west-1:123:stream/testStream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-east-1.amazonaws.com'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint with FIPS enabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=False, OperationType='data', ResourceARN='arn:aws-cn:kinesis:cn-northwest-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.cn-northwest-1.amazonaws.com.cn'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint with FIPS and DualStack enabled for cn regions."""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=True, OperationType='data', ResourceARN='arn:aws-cn:kinesis:cn-northwest-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.cn-northwest-1.api.amazonwebservices.com.cn'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-east-1.c2s.ic.gov'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-west-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-west-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-west-1.c2s.ic.gov'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint targeting data operation type in ADC regions"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ResourceARN='arn:aws-iso-b:kinesis:us-isob-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-isob-east-1.sc2s.sgov.gov'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint with fips targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-iso-east-1.c2s.ic.gov'

def test_resourcearn_as_streamarn_test__account_e():
    """ResourceARN as StreamARN test: Account endpoint with fips targeting data operation type in ADC regions"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', ResourceARN='arn:aws-iso-b:kinesis:us-isob-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-isob-east-1.sc2s.sgov.gov'

def test_resourcearn_as_consumerarn_test__invalid():
    """ResourceARN as ConsumerARN test: Invalid ARN: partition missing from ARN."""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn::kinesis:us-west-2:123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Failed to parse ARN.')):
        resolve(params)

def test_resourcearn_as_consumerarn_test__invalid():
    """ResourceARN as ConsumerARN test: Invalid ARN: partitions mismatch."""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:us-west-2:123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape("Partition: aws from ARN doesn't match with partition name: aws-us-gov.")):
        resolve(params)

def test_resourcearn_as_consumerarn_test__invalid():
    """ResourceARN as ConsumerARN test: Invalid ARN: Not Kinesis"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:s3:us-west-2:123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The ARN was not for the Kinesis service, found: s3.')):
        resolve(params)

def test_resourcearn_as_consumerarn_test__invalid():
    """ResourceARN as ConsumerARN test: Invalid ARN: Region is missing in ARN"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis::123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid region.')):
        resolve(params)

def test_resourcearn_as_consumerarn_test__invalid():
    """ResourceARN as ConsumerARN test: Invalid ARN: Region is empty string in ARN"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:  :123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid region.')):
        resolve(params)

def test_resourcearn_as_consumerarn_test__invalid():
    """ResourceARN as ConsumerARN test: Invalid ARN: Invalid account id"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:us-east-1::stream/testStream/consumer/test-consumer:1525898737', OperationType='control')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid account id.')):
        resolve(params)

def test_resourcearn_as_consumerarn_test__invalid():
    """ResourceARN as ConsumerARN test: Invalid ARN: Invalid account id"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:us-east-1:   :stream/testStream/consumer/test-consumer:1525898737', OperationType='control')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Invalid account id.')):
        resolve(params)

def test_resourcearn_as_consumerarn_test__invalid():
    """ResourceARN as ConsumerARN test: Invalid ARN: Kinesis ARNs only support stream arn/consumer arn types"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:us-east-1:123:accesspoint/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape("Invalid ARN: Kinesis ARNs don't support `accesspoint` arn types.")):
        resolve(params)

def test_resourcearn_as_consumerarn_test__operati():
    """ResourceARN as ConsumerARN test: OperationType not set"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, ResourceARN='arn:aws:kinesis:us-east-1:123456789012:stream/testStream/consumer/test-consumer:1525898737')
    with pytest.raises(EndpointError, match=re.escape('Operation Type is not set. Please contact service team for resolution.')):
        resolve(params)

def test_resourcearn_as_consumerarn_test__custom_():
    """ResourceARN as ConsumerARN test: Custom Endpoint is specified"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-east-1.amazonaws.com'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-east-1.amazonaws.com'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint with fips targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.us-east-1.amazonaws.com'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint with fips targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis-fips.us-east-1.amazonaws.com'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint with Dual Stack and FIPS enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis-fips.us-east-1.api.aws'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint with Dual Stack enabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=True, OperationType='data', ResourceARN='arn:aws:kinesis:us-west-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-west-1.api.aws'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint with FIPS and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws:kinesis:us-west-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-west-1.amazonaws.com'

def test_resourcearn_as_consumerarn_test__regionm():
    """ResourceARN as ConsumerARN test: RegionMismatch: client region should be used for endpoint region"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ResourceARN='arn:aws:kinesis:us-west-1:123:stream/testStream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-east-1.amazonaws.com'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint with FIPS enabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=False, OperationType='data', ResourceARN='arn:aws-cn:kinesis:cn-northwest-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.cn-northwest-1.amazonaws.com.cn'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint with FIPS and DualStack enabled for cn regions."""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=True, OperationType='data', ResourceARN='arn:aws-cn:kinesis:cn-northwest-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis-fips.cn-northwest-1.api.amazonwebservices.com.cn'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-east-1.c2s.ic.gov'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-west-1', UseFIPS=False, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-west-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-iso-west-1.c2s.ic.gov'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint targeting data operation type in ADC regions"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', ResourceARN='arn:aws-iso-b:kinesis:us-isob-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-isob-east-1.sc2s.sgov.gov'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint with fips targeting control operation type in ADC regions"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', ResourceARN='arn:aws-iso:kinesis:us-iso-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-iso-east-1.c2s.ic.gov'

def test_resourcearn_as_consumerarn_test__account():
    """ResourceARN as ConsumerARN test: Account endpoint with fips targeting data operation type in ADC regions"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', ResourceARN='arn:aws-iso-b:kinesis:us-isob-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://kinesis-fips.us-isob-east-1.sc2s.sgov.gov'

def test_streamid_test__operationtype_not_set_wit():
    """StreamId test: OperationType not set with StreamId"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, StreamId='af4lwng4k01746835071-xyz')
    with pytest.raises(EndpointError, match=re.escape('Operation Type is not set. Please contact service team for resolution.')):
        resolve(params)

def test_streamid_test__stream_endpoint_targeting():
    """StreamId test: Stream endpoint targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-xyz', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis.us-east-1.amazonaws.com'

def test_streamid_test__stream_endpoint_targeting():
    """StreamId test: Stream endpoint targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', StreamId='af4lwng4k01746835071-xyz', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis.us-east-1.amazonaws.com'

def test_streamid_test__stream_endpoint_with_fips():
    """StreamId test: Stream endpoint with fips targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', StreamId='af4lwng4k01746835071-xyz', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis-fips.us-east-1.amazonaws.com'

def test_streamid_test__stream_endpoint_with_fips():
    """StreamId test: Stream endpoint with fips targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-xyz', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis-fips.us-east-1.amazonaws.com'

def test_streamid_test__stream_endpoint_with_dual():
    """StreamId test: Stream endpoint with Dual Stack and FIPS enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', StreamId='af4lwng4k01746835071-xyz', StreamARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis-fips.us-east-1.api.aws'

def test_streamid_test__stream_endpoint_with_dual():
    """StreamId test: Stream endpoint with Dual Stack enabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=True, OperationType='data', StreamId='af4lwng4k01746835071-xyz', StreamARN='arn:aws:kinesis:us-west-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis.us-west-1.api.aws'

def test_streamid_test__stream_endpoint_with_fips():
    """StreamId test: Stream endpoint with FIPS and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-xyz', StreamARN='arn:aws:kinesis:us-west-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis.us-west-1.amazonaws.com'

def test_streamid_test__stream_endpoint_fips_and_():
    """StreamId test: Stream endpoint FIPS and DualStack disabled with endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-xyz', Endpoint='kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis-pod1.us-east-1.amazonaws.com'

def test_streamid_test__stream_endpoint_targeting():
    """StreamId test: Stream endpoint targeting data operation type with endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', StreamId='af4lwng4k01746835071-xyz', Endpoint='kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis-pod1.us-east-1.amazonaws.com'

def test_streamid_test__stream_endpoint_with_fips():
    """StreamId test: Stream endpoint with fips targeting data operation type with endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', StreamId='af4lwng4k01746835071-xyz', Endpoint='kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis-pod1-fips.us-east-1.amazonaws.com'

def test_streamid_test__stream_endpoint_with_fips():
    """StreamId test: Stream endpoint with fips targeting control operation type with endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-xyz', Endpoint='kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis-pod1-fips.us-east-1.amazonaws.com'

def test_streamid_test__stream_endpoint_with_dual():
    """StreamId test: Stream endpoint with Dual Stack and FIPS enabled with endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', StreamId='af4lwng4k01746835071-xyz', Endpoint='kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis-pod1-fips.us-east-1.api.aws'

def test_streamid_test__stream_endpoint_with_dual():
    """StreamId test: Stream endpoint with Dual Stack enabled with endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, OperationType='data', StreamId='af4lwng4k01746835071-xyz', Endpoint='kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis-pod1.us-east-1.api.aws'

def test_streamid_test__stream_endpoint_targeting():
    """StreamId test: Stream endpoint targeting data operation type with https endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', StreamId='af4lwng4k01746835071-xyz', Endpoint='https://kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis-pod1.us-east-1.amazonaws.com'

def test_streamid_test__https_endpoint_with_fips_():
    """StreamId test: HTTPS endpoint with FIPS enabled targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-xyz', Endpoint='https://kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis-pod1-fips.us-east-1.amazonaws.com'

def test_streamid_test__https_endpoint_with_fips_():
    """StreamId test: HTTPS endpoint with FIPS enabled targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, OperationType='data', StreamId='af4lwng4k01746835071-xyz', Endpoint='https://kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis-pod1-fips.us-east-1.amazonaws.com'

def test_streamid_test__https_endpoint_with_duals():
    """StreamId test: HTTPS endpoint with DualStack enabled targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, OperationType='control', StreamId='af4lwng4k01746835071-xyz', Endpoint='https://kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis-pod1.us-east-1.api.aws'

def test_streamid_test__https_endpoint_with_duals():
    """StreamId test: HTTPS endpoint with DualStack enabled targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, OperationType='data', StreamId='af4lwng4k01746835071-xyz', Endpoint='https://kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis-pod1.us-east-1.api.aws'

def test_streamid_test__https_endpoint_with_fips_():
    """StreamId test: HTTPS endpoint with FIPS and DualStack enabled targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='control', StreamId='af4lwng4k01746835071-xyz', Endpoint='https://kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis-pod1-fips.us-east-1.api.aws'

def test_streamid_test__https_endpoint_with_fips_():
    """StreamId test: HTTPS endpoint with FIPS and DualStack enabled targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, OperationType='data', StreamId='af4lwng4k01746835071-xyz', Endpoint='https://kinesis-pod1.us-east-1.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis-pod1-fips.us-east-1.api.aws'

def test_streamid_test__https_endpoint_with_fips_():
    """StreamId test: HTTPS endpoint with FIPS enabled in different region"""
    params = EndpointParams(Region='us-west-2', UseFIPS=True, UseDualStack=False, OperationType='data', StreamId='af4lwng4k01746835071-xyz', Endpoint='https://kinesis-pod2.us-west-2.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis-pod2-fips.us-west-2.amazonaws.com'

def test_streamid_test__https_endpoint_with_duals():
    """StreamId test: HTTPS endpoint with DualStack enabled in different region"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=True, OperationType='control', StreamId='af4lwng4k01746835071-xyz', Endpoint='https://kinesis-pod2.us-west-2.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis-pod2.us-west-2.api.aws'

def test_streamid_test__stream_endpoint_with_cons():
    """StreamId test: Stream endpoint with ConsumerARN targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-xyz', ConsumerARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis.us-east-1.amazonaws.com'

def test_streamid_test__stream_endpoint_with_cons():
    """StreamId test: Stream endpoint with ConsumerARN targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', StreamId='af4lwng4k01746835071-xyz', ConsumerARN='arn:aws:kinesis:us-east-1:123:stream/test-stream/consumer/test-consumer:1525898737')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis.us-east-1.amazonaws.com'

def test_streamid_test__stream_endpoint_with_reso():
    """StreamId test: Stream endpoint with ResourceARN targeting control operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-xyz', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.control-kinesis.us-east-1.amazonaws.com'

def test_streamid_test__stream_endpoint_with_reso():
    """StreamId test: Stream endpoint with ResourceARN targeting data operation type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', StreamId='af4lwng4k01746835071-xyz', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://af4lwng4k01746835071.xyz.data-kinesis.us-east-1.amazonaws.com'

def test_streamid_test__invalid_streamid_with_arn():
    """StreamId test: Invalid StreamId with ARN"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, OperationType='data', StreamId='af4lwng4k01746835071=xyz', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.data-kinesis.us-east-1.amazonaws.com'

def test_streamid_test__invalid_streamid_with_cus():
    """StreamId test: Invalid streamId with custom endpoint"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071=xyz', Endpoint='https://kinesis-pod2.us-west-2.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://kinesis-pod2.us-west-2.amazonaws.com'

def test_streamid_test__invalid_streamid():
    """StreamId test: Invalid streamId"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071=xyz')
    result = resolve(params)
    assert result.url == 'https://kinesis.us-west-2.amazonaws.com'

def test_streamid_test__invalid_streamid_with_cus():
    """StreamId test: Invalid streamId with custom endpoint and ARN"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071=xyz', Endpoint='https://kinesis-pod2.us-west-2.amazonaws.com', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://kinesis-pod2.us-west-2.amazonaws.com'

def test_streamid_test__invalid_streamid_with_lon():
    """StreamId test: Invalid streamId with longer prefix"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k0174683507123-xyz', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-west-2.amazonaws.com'

def test_streamid_test__invalid_streamid_with_sho():
    """StreamId test: Invalid streamId with shorter prefix"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835-xyz', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-west-2.amazonaws.com'

def test_streamid_test__invalid_streamid_with_lon():
    """StreamId test: Invalid streamId with longer suffix"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-wxyz', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-west-2.amazonaws.com'

def test_streamid_test__invalid_streamid_with_sho():
    """StreamId test: Invalid streamId with shorter suffix"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, OperationType='control', StreamId='af4lwng4k01746835071-yz', ResourceARN='arn:aws:kinesis:us-east-1:123:stream/test-stream')
    result = resolve(params)
    assert result.url == 'https://123.control-kinesis.us-west-2.amazonaws.com'