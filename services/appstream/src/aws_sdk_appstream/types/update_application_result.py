"""Generated from Smithy shape ``com.amazonaws.appstream#UpdateApplicationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.application


class UpdateApplicationResult(TypedDict):
    application: NotRequired["aws_sdk_appstream.types.application.Application"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateApplicationResult) -> dict:
    out: dict = {}
    if "application" in value:
        import aws_sdk_appstream.types.application

        out["Application"] = aws_sdk_appstream.types.application.serialize_aws_json_1_1(
            value["application"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateApplicationResult:
    out: UpdateApplicationResult = {}  # type: ignore[typeddict-item]
    if "Application" in data:
        import aws_sdk_appstream.types.application

        out["application"] = (
            aws_sdk_appstream.types.application.deserialize_aws_json_1_1(
                data["Application"]
            )
        )
    return out
