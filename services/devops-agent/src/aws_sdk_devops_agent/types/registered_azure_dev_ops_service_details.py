"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredAzureDevOpsServiceDetails``."""

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError


class RegisteredAzureDevOpsServiceDetails(TypedDict, closed=True):
    organization_name: "str"
    """<p>The Azure DevOps Organization name associated with the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredAzureDevOpsServiceDetails) -> dict:
    out: dict = {}
    out["organizationName"] = value["organization_name"]
    return out


def deserialize_json(data: dict) -> RegisteredAzureDevOpsServiceDetails:
    out: RegisteredAzureDevOpsServiceDetails = {}  # type: ignore[typeddict-item]
    if "organizationName" in data:
        out["organization_name"] = data["organizationName"]
    else:
        raise DeserializationError(
            "RegisteredAzureDevOpsServiceDetails.organization_name required"
        )
    return out
