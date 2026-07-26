"""Generated from Smithy shape ``com.amazonaws.devicefarm#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_device_farm.types.device_farm_arn
    import capo_device_farm.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_device_farm.types.device_farm_arn.DeviceFarmArn"
    """<p>The Amazon Resource Name (ARN) of the resource or resources from which to delete tags. You can associate tags with the following Device Farm resources: <code>PROJECT</code>, <code>TESTGRID_PROJECT</code>, <code>RUN</code>, <code>NETWORK_PROFILE</code>, <code>INSTANCE_PROFILE</code>, <code>DEVICE_INSTANCE</code>, <code>SESSION</code>, <code>DEVICE_POOL</code>, <code>DEVICE</code>, and <code>VPCE_CONFIGURATION</code>.</p>"""
    tag_keys: "capo_device_farm.types.tag_key_list.TagKeyList"
    """<p>The keys of the tags to be removed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_device_farm.types.tag_key_list

    out["TagKeys"] = capo_device_farm.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "TagKeys" in data:
        import capo_device_farm.types.tag_key_list

        out["tag_keys"] = capo_device_farm.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
