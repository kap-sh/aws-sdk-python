"""Generated from Smithy shape ``com.amazonaws.schemas#ListRegistriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__integer
    import aws_sdk_schemas.types.__string


class ListRegistriesRequest(TypedDict, closed=True):
    limit: NotRequired["aws_sdk_schemas.types.__integer.__integer"]
    next_token: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.</p>"""
    registry_name_prefix: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>Specifying this limits the results to only those registry names that start with the specified prefix.</p>"""
    scope: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>Can be set to Local or AWS to limit responses to your custom registries, or the ones provided by AWS.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRegistriesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRegistriesRequest:
    out: ListRegistriesRequest = {}  # type: ignore[typeddict-item]
    return out
