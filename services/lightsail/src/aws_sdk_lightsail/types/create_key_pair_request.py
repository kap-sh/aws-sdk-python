"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateKeyPairRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.tag_list


class CreateKeyPairRequest(TypedDict):
    key_pair_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name for your new key pair.</p>"""
    tags: NotRequired["aws_sdk_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateKeyPairRequest) -> dict:
    out: dict = {}
    out["keyPairName"] = value["key_pair_name"]
    if "tags" in value:
        import aws_sdk_lightsail.types.tag_list

        out["tags"] = aws_sdk_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateKeyPairRequest:
    out: CreateKeyPairRequest = {}  # type: ignore[typeddict-item]
    if "keyPairName" in data:
        out["key_pair_name"] = data["keyPairName"]
    else:
        raise DeserializationError("CreateKeyPairRequest.key_pair_name required")
    if "tags" in data:
        import aws_sdk_lightsail.types.tag_list

        out["tags"] = aws_sdk_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
