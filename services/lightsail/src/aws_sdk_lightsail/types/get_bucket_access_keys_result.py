"""Generated from Smithy shape ``com.amazonaws.lightsail#GetBucketAccessKeysResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.access_key_list


class GetBucketAccessKeysResult(TypedDict, closed=True):
    access_keys: NotRequired["aws_sdk_lightsail.types.access_key_list.AccessKeyList"]
    """<p>An object that describes the access keys for the specified bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBucketAccessKeysResult) -> dict:
    out: dict = {}
    if "access_keys" in value:
        import aws_sdk_lightsail.types.access_key_list

        out["accessKeys"] = (
            aws_sdk_lightsail.types.access_key_list.serialize_aws_json_1_1(
                value["access_keys"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBucketAccessKeysResult:
    out: GetBucketAccessKeysResult = {}  # type: ignore[typeddict-item]
    if "accessKeys" in data:
        import aws_sdk_lightsail.types.access_key_list

        out["access_keys"] = (
            aws_sdk_lightsail.types.access_key_list.deserialize_aws_json_1_1(
                data["accessKeys"]
            )
        )
    return out
