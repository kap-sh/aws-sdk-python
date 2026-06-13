"""Generated from Smithy shape ``com.amazonaws.entityresolution#ListProviderServicesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.entity_name
    import aws_sdk_entityresolution.types.next_token


class ListProviderServicesInput(TypedDict):
    next_token: NotRequired["aws_sdk_entityresolution.types.next_token.NextToken"]
    """<p>The pagination token from the previous API call.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of objects returned per page.</p>"""
    provider_name: NotRequired["aws_sdk_entityresolution.types.entity_name.EntityName"]
    """<p>The name of the provider. This name is typically the company name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProviderServicesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProviderServicesInput:
    out: ListProviderServicesInput = {}  # type: ignore[typeddict-item]
    return out
