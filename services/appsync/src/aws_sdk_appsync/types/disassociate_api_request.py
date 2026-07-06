"""Generated from Smithy shape ``com.amazonaws.appsync#DisassociateApiRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.domain_name


class DisassociateApiRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_appsync.types.domain_name.DomainName"
    """<p>The domain name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateApiRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateApiRequest:
    out: DisassociateApiRequest = {}  # type: ignore[typeddict-item]
    return out
