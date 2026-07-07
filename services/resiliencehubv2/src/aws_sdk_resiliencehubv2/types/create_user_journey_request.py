"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreateUserJourneyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.client_token
    import aws_sdk_resiliencehubv2.types.entity_description
    import aws_sdk_resiliencehubv2.types.entity_label


class CreateUserJourneyRequest(TypedDict, closed=True):
    system_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    name: "aws_sdk_resiliencehubv2.types.entity_label.EntityLabel"
    description: NotRequired[
        "aws_sdk_resiliencehubv2.types.entity_description.EntityDescription"
    ]
    policy_arn: NotRequired["aws_sdk_resiliencehubv2.types.arn.Arn"]
    client_token: NotRequired["aws_sdk_resiliencehubv2.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserJourneyRequest) -> dict:
    out: dict = {}
    out["systemArn"] = value["system_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateUserJourneyRequest:
    out: CreateUserJourneyRequest = {}  # type: ignore[typeddict-item]
    if "systemArn" in data:
        out["system_arn"] = data["systemArn"]
    else:
        raise DeserializationError("CreateUserJourneyRequest.system_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateUserJourneyRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
