import pytest
from aws_sdk_cloudfront_keyvaluestore._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_cloudfront_keyvaluestore._rule_engine._endpoint_runtime import EndpointError
import re
import zapros

def test_1_fips_should_error():
    """FIPS should error"""
    params = EndpointParams(UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS is not supported with CloudFront-KeyValueStore.')):
        resolve(params)

def test_2_kvs_arn_must_be_provided_to_use_this_ser():
    """KVS ARN must be provided to use this service"""
    params = EndpointParams()
    with pytest.raises(EndpointError, match=re.escape('KVS ARN must be provided to use this service')):
        resolve(params)

def test_3_kvs_arn_must_be_a_valid_arn():
    """KVS ARN must be a valid ARN"""
    params = EndpointParams(KvsARN='not-a-valid-arn')
    with pytest.raises(EndpointError, match=re.escape('KVS ARN must be a valid ARN')):
        resolve(params)

def test_4_provided_arn_was_not_a_valid_cloudfront_():
    """Provided ARN was not a valid CloudFront Service ARN. Found: `notcloudfront`"""
    params = EndpointParams(KvsARN='arn:aws:notcloudfront::123456789012:key-value-store/my-first-kvs-e10b1dce4f394248811e77167e0451ba')
    with pytest.raises(EndpointError, match=re.escape('Provided ARN is not a valid CloudFront Service ARN. Found: `notcloudfront`')):
        resolve(params)

def test_5_provided_arn_must_be_a_global_resource_a():
    """Provided ARN must be a global resource ARN. Found: `us-west-2`"""
    params = EndpointParams(KvsARN='arn:aws:cloudfront:us-west-2:123456789012:key-value-store/my-first-kvs-e10b1dce4f394248811e77167e0451ba')
    with pytest.raises(EndpointError, match=re.escape('Provided ARN must be a global resource ARN. Found: `us-west-2`')):
        resolve(params)

def test_6_arn_resource_type_is_invalid__expected__():
    """ARN resource type is invalid. Expected `key-value-store`, found: `some-other-resource-type`"""
    params = EndpointParams(KvsARN='arn:aws:cloudfront::123456789012:some-other-resource-type/my-first-kvs-e10b1dce4f394248811e77167e0451ba')
    with pytest.raises(EndpointError, match=re.escape('ARN resource type is invalid. Expected `key-value-store`, found: `some-other-resource-type`')):
        resolve(params)

def test_7_cloudfront_keyvaluestore_is_not_supporte():
    """CloudFront-KeyValueStore is not supported in partition `aws-cn`"""
    params = EndpointParams(KvsARN='arn:aws-cn:cloudfront::123456789012:key-value-store/my-first-kvs-e10b1dce4f394248811e77167e0451ba')
    with pytest.raises(EndpointError, match=re.escape('CloudFront-KeyValueStore is not supported in partition `aws-cn`')):
        resolve(params)

def test_8_cloudfront_keyvaluestore_is_not_supporte():
    """CloudFront-KeyValueStore is not supported in partition `aws-us-gov`"""
    params = EndpointParams(KvsARN='arn:aws-us-gov:cloudfront::123456789012:key-value-store/my-first-kvs-e10b1dce4f394248811e77167e0451ba')
    with pytest.raises(EndpointError, match=re.escape('CloudFront-KeyValueStore is not supported in partition `aws-us-gov`')):
        resolve(params)

def test_9_valid_account_based_endpoint():
    """Valid account based endpoint"""
    params = EndpointParams(KvsARN='arn:aws:cloudfront::123456789012:key-value-store/my-first-kvs-e10b1dce4f394248811e77167e0451ba')
    result = resolve(params)
    assert result.url == 'https://123456789012.cloudfront-kvs.global.api.aws'

def test_10_valid_account_based_endpoint__with_sdk_r():
    """Valid account based endpoint, with SDK region"""
    params = EndpointParams(KvsARN='arn:aws:cloudfront::123456789012:key-value-store/my-first-kvs-e10b1dce4f394248811e77167e0451ba', Region='us-west-2')
    result = resolve(params)
    assert result.url == 'https://123456789012.cloudfront-kvs.global.api.aws'

def test_11_valid_arn__different_partition__should_e():
    """Valid ARN, different partition, should error"""
    params = EndpointParams(KvsARN='arn:aws:cloudfront::123456789012:key-value-store/my-first-kvs-e10b1dce4f394248811e77167e0451ba', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Client was configured for partition `aws-cn` but Kvs ARN has `aws`')):
        resolve(params)

def test_12_valid_account_based_endpoint_with_fips__():
    """Valid account based endpoint with FIPS, should error"""
    params = EndpointParams(KvsARN='arn:aws:cloudfront::123456789012:key-value-store/my-first-kvs-e10b1dce4f394248811e77167e0451ba', Region='us-east-1', UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS is not supported with CloudFront-KeyValueStore.')):
        resolve(params)

def test_13_custom_sdk_endpoint_override():
    """Custom sdk endpoint override"""
    params = EndpointParams(KvsARN='arn:aws:cloudfront::123456789012:key-value-store/my-first-kvs-e10b1dce4f394248811e77167e0451ba', Region='us-east-1', Endpoint='https://my-override.example.com')
    result = resolve(params)
    assert result.url == 'https://123456789012.my-override.example.com'

def test_14_custom_sdk_endpoint_override_with_path_a():
    """Custom sdk endpoint override with path and http"""
    params = EndpointParams(KvsARN='arn:aws:cloudfront::123456789012:key-value-store/my-first-kvs-e10b1dce4f394248811e77167e0451ba', Endpoint='http://my-override.example.com/custom-path')
    result = resolve(params)
    assert result.url == 'http://123456789012.my-override.example.com/custom-path'

def test_15_custom_override_with_different_partition():
    """Custom override with different partition should error"""
    params = EndpointParams(KvsARN='arn:aws:cloudfront::123456789012:key-value-store/my-first-kvs-e10b1dce4f394248811e77167e0451ba', Region='us-gov-east-1', Endpoint='https://my-override.example.com')
    with pytest.raises(EndpointError, match=re.escape('Client was configured for partition `aws-us-gov` but Kvs ARN has `aws`')):
        resolve(params)