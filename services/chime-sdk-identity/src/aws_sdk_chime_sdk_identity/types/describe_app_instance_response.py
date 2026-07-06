"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#DescribeAppInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.app_instance


class DescribeAppInstanceResponse(TypedDict, closed=True):
    app_instance: NotRequired[
        "aws_sdk_chime_sdk_identity.types.app_instance.AppInstance"
    ]
    """<p>The ARN, metadata, created and last-updated timestamps, and the name of the <code>AppInstance</code>. All timestamps use epoch milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppInstanceResponse) -> dict:
    out: dict = {}
    if "app_instance" in value:
        import aws_sdk_chime_sdk_identity.types.app_instance

        out["AppInstance"] = (
            aws_sdk_chime_sdk_identity.types.app_instance.serialize_json(
                value["app_instance"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAppInstanceResponse:
    out: DescribeAppInstanceResponse = {}  # type: ignore[typeddict-item]
    if "AppInstance" in data:
        import aws_sdk_chime_sdk_identity.types.app_instance

        out["app_instance"] = (
            aws_sdk_chime_sdk_identity.types.app_instance.deserialize_json(
                data["AppInstance"]
            )
        )
    return out
