"""Generated from Smithy shape ``com.amazonaws.securitylake#CreateCustomLogSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.custom_log_source_resource


class CreateCustomLogSourceResponse(TypedDict, closed=True):
    source: NotRequired[
        "aws_sdk_securitylake.types.custom_log_source_resource.CustomLogSourceResource"
    ]
    """<p>The third-party custom source that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCustomLogSourceResponse) -> dict:
    out: dict = {}
    if "source" in value:
        import aws_sdk_securitylake.types.custom_log_source_resource

        out["source"] = (
            aws_sdk_securitylake.types.custom_log_source_resource.serialize_json(
                value["source"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateCustomLogSourceResponse:
    out: CreateCustomLogSourceResponse = {}  # type: ignore[typeddict-item]
    if "source" in data:
        import aws_sdk_securitylake.types.custom_log_source_resource

        out["source"] = (
            aws_sdk_securitylake.types.custom_log_source_resource.deserialize_json(
                data["source"]
            )
        )
    return out
