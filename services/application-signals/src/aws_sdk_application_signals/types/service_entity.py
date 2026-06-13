"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceEntity``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ServiceEntity(TypedDict):
    type: NotRequired["str"]
    """<p>The type of the service entity.</p>"""
    name: NotRequired["str"]
    """<p>The name of the service.</p>"""
    environment: NotRequired["str"]
    """<p>The environment where the service is deployed.</p>"""
    aws_account_id: NotRequired["str"]
    """<p>The Amazon Web Services account ID where the service is located. Provide this value only for cross-account access.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceEntity) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "name" in value:
        out["Name"] = value["name"]
    if "environment" in value:
        out["Environment"] = value["environment"]
    if "aws_account_id" in value:
        out["AwsAccountId"] = value["aws_account_id"]
    return out


def deserialize_json(data: dict) -> ServiceEntity:
    out: ServiceEntity = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Environment" in data:
        out["environment"] = data["Environment"]
    if "AwsAccountId" in data:
        out["aws_account_id"] = data["AwsAccountId"]
    return out
