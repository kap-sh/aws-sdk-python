"""Generated from Smithy shape ``com.amazonaws.configservice#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.amazon_resource_name
    import aws_sdk_config_service.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_config_service.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. The following resources are supported:</p> <ul> <li> <p> <code>ConfigurationRecorder</code> </p> </li> <li> <p> <code>ConfigRule</code> </p> </li> <li> <p> <code>OrganizationConfigRule</code> </p> </li> <li> <p> <code>ConformancePack</code> </p> </li> <li> <p> <code>OrganizationConformancePack</code> </p> </li> <li> <p> <code>ConfigurationAggregator</code> </p> </li> <li> <p> <code>AggregationAuthorization</code> </p> </li> <li> <p> <code>StoredQuery</code> </p> </li> </ul>"""
    tag_keys: "aws_sdk_config_service.types.tag_key_list.TagKeyList"
    """<p>The keys of the tags to be removed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_config_service.types.tag_key_list

    out["TagKeys"] = aws_sdk_config_service.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "TagKeys" in data:
        import aws_sdk_config_service.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_config_service.types.tag_key_list.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
