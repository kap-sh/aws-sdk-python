"""Generated from Smithy shape ``com.amazonaws.route53resolver#DeleteOutpostResolverRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53resolver.types.resource_id


class DeleteOutpostResolverRequest(TypedDict, closed=True):
    id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>A unique string that identifies the Resolver on the Outpost.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteOutpostResolverRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteOutpostResolverRequest:
    out: DeleteOutpostResolverRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("DeleteOutpostResolverRequest.id required")
    return out
