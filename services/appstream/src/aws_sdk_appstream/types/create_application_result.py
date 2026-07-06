"""Generated from Smithy shape ``com.amazonaws.appstream#CreateApplicationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.application


class CreateApplicationResult(TypedDict, closed=True):
    application: NotRequired["aws_sdk_appstream.types.application.Application"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApplicationResult) -> dict:
    out: dict = {}
    if "application" in value:
        import aws_sdk_appstream.types.application

        out["Application"] = aws_sdk_appstream.types.application.serialize_aws_json_1_1(
            value["application"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApplicationResult:
    out: CreateApplicationResult = {}  # type: ignore[typeddict-item]
    if "Application" in data:
        import aws_sdk_appstream.types.application

        out["application"] = (
            aws_sdk_appstream.types.application.deserialize_aws_json_1_1(
                data["Application"]
            )
        )
    return out
