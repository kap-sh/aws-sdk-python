"""Generated from Smithy shape ``com.amazonaws.applicationinsights#CreateApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.application_info


class CreateApplicationResponse(TypedDict, closed=True):
    application_info: NotRequired[
        "aws_sdk_application_insights.types.application_info.ApplicationInfo"
    ]
    """<p>Information about the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApplicationResponse) -> dict:
    out: dict = {}
    if "application_info" in value:
        import aws_sdk_application_insights.types.application_info

        out["ApplicationInfo"] = (
            aws_sdk_application_insights.types.application_info.serialize_aws_json_1_1(
                value["application_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApplicationResponse:
    out: CreateApplicationResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationInfo" in data:
        import aws_sdk_application_insights.types.application_info

        out["application_info"] = (
            aws_sdk_application_insights.types.application_info.deserialize_aws_json_1_1(
                data["ApplicationInfo"]
            )
        )
    return out
