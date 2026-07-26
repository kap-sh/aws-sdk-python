"""Generated from Smithy shape ``com.amazonaws.appstream#UpdateApplicationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.application


class UpdateApplicationResult(TypedDict, closed=True):
    application: NotRequired["capo_appstream.types.application.Application"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateApplicationResult) -> dict:
    out: dict = {}
    if "application" in value:
        import capo_appstream.types.application

        out["Application"] = capo_appstream.types.application.serialize_aws_json_1_1(
            value["application"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateApplicationResult:
    out: UpdateApplicationResult = {}  # type: ignore[typeddict-item]
    if "Application" in data:
        import capo_appstream.types.application

        out["application"] = capo_appstream.types.application.deserialize_aws_json_1_1(
            data["Application"]
        )
    return out
