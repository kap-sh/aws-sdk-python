"""Generated from Smithy shape ``com.amazonaws.connect#DescribeAttachedFilesConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.attached_files_configuration


class DescribeAttachedFilesConfigurationResponse(TypedDict, closed=True):
    attached_files_configuration: (
        "aws_sdk_connect.types.attached_files_configuration.AttachedFilesConfiguration"
    )
    """<p>Information about the attached files configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAttachedFilesConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.attached_files_configuration

    out["AttachedFilesConfiguration"] = (
        aws_sdk_connect.types.attached_files_configuration.serialize_json(
            value["attached_files_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeAttachedFilesConfigurationResponse:
    out: DescribeAttachedFilesConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "AttachedFilesConfiguration" in data:
        import aws_sdk_connect.types.attached_files_configuration

        out["attached_files_configuration"] = (
            aws_sdk_connect.types.attached_files_configuration.deserialize_json(
                data["AttachedFilesConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAttachedFilesConfigurationResponse.attached_files_configuration required"
        )
    return out
