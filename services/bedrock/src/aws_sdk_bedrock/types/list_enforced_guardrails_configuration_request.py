"""Generated from Smithy shape ``com.amazonaws.bedrock#ListEnforcedGuardrailsConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.pagination_token


class ListEnforcedGuardrailsConfigurationRequest(TypedDict):
    next_token: NotRequired["aws_sdk_bedrock.types.pagination_token.PaginationToken"]
    """<p>Opaque continuation token of previous paginated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnforcedGuardrailsConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEnforcedGuardrailsConfigurationRequest:
    out: ListEnforcedGuardrailsConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
