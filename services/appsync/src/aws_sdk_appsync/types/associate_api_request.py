"""Generated from Smithy shape ``com.amazonaws.appsync#AssociateApiRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.domain_name
    import aws_sdk_appsync.types.string


class AssociateApiRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_appsync.types.domain_name.DomainName"
    """<p>The domain name.</p>"""
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The API ID. Private APIs can not be associated with custom domains.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateApiRequest) -> dict:
    out: dict = {}
    out["apiId"] = value["api_id"]
    return out


def deserialize_json(data: dict) -> AssociateApiRequest:
    out: AssociateApiRequest = {}  # type: ignore[typeddict-item]
    if "apiId" in data:
        out["api_id"] = data["apiId"]
    else:
        raise DeserializationError("AssociateApiRequest.api_id required")
    return out
