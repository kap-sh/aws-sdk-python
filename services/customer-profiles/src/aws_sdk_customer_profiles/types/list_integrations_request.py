"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListIntegrationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.max_size100
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.optional_boolean
    import aws_sdk_customer_profiles.types.token


class ListIntegrationsRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous ListIntegrations API call.</p>"""
    max_results: NotRequired["aws_sdk_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of objects returned per page.</p>"""
    include_hidden: NotRequired[
        "aws_sdk_customer_profiles.types.optional_boolean.optionalBoolean"
    ]
    """<p>Boolean to indicate if hidden integration should be returned. Defaults to <code>False</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIntegrationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListIntegrationsRequest:
    out: ListIntegrationsRequest = {}  # type: ignore[typeddict-item]
    return out
