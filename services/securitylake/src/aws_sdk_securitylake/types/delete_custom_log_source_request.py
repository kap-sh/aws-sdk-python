"""Generated from Smithy shape ``com.amazonaws.securitylake#DeleteCustomLogSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.custom_log_source_name
    import aws_sdk_securitylake.types.custom_log_source_version


class DeleteCustomLogSourceRequest(TypedDict, closed=True):
    source_name: "aws_sdk_securitylake.types.custom_log_source_name.CustomLogSourceName"
    """<p>The source name of custom log source that you want to delete.</p>"""
    source_version: NotRequired[
        "aws_sdk_securitylake.types.custom_log_source_version.CustomLogSourceVersion"
    ]
    """<p>The source version for the third-party custom source. You can limit the custom source removal to the specified source version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCustomLogSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCustomLogSourceRequest:
    out: DeleteCustomLogSourceRequest = {}  # type: ignore[typeddict-item]
    return out
