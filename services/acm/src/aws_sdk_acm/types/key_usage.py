"""Generated from Smithy shape ``com.amazonaws.acm#KeyUsage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_acm.types.key_usage_name


class KeyUsage(TypedDict, closed=True):
    name: NotRequired["aws_sdk_acm.types.key_usage_name.KeyUsageName"]
    """<p>A string value that contains a Key Usage extension name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyUsage) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_acm.types.key_usage_name

        out["Name"] = aws_sdk_acm.types.key_usage_name.serialize_aws_json_1_1(
            value["name"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> KeyUsage:
    out: KeyUsage = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_acm.types.key_usage_name

        out["name"] = aws_sdk_acm.types.key_usage_name.deserialize_aws_json_1_1(
            data["Name"]
        )
    return out
