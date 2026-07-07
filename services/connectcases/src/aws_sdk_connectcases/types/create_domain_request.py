"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.domain_name


class CreateDomainRequest(TypedDict, closed=True):
    name: "aws_sdk_connectcases.types.domain_name.DomainName"
    """<p>The name for your Cases domain. It must be unique for your Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateDomainRequest:
    out: CreateDomainRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDomainRequest.name required")
    return out
