"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name


class GetDomainRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDomainRequest:
    out: GetDomainRequest = {}  # type: ignore[typeddict-item]
    return out
