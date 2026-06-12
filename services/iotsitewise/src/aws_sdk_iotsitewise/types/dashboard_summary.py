"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DashboardSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.description
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.name
    import aws_sdk_iotsitewise.types.timestamp


class DashboardSummary(TypedDict):
    id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the dashboard.</p>"""
    name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The name of the dashboard</p>"""
    description: NotRequired["aws_sdk_iotsitewise.types.description.Description"]
    """<p>The dashboard's description.</p>"""
    creation_date: NotRequired["aws_sdk_iotsitewise.types.timestamp.Timestamp"]
    """<p>The date the dashboard was created, in Unix epoch time.</p>"""
    last_update_date: NotRequired["aws_sdk_iotsitewise.types.timestamp.Timestamp"]
    """<p>The date the dashboard was last updated, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashboardSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "creation_date" in value:
        import aws_sdk_iotsitewise.types.timestamp

        out["creationDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "last_update_date" in value:
        import aws_sdk_iotsitewise.types.timestamp

        out["lastUpdateDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
            value["last_update_date"]
        )
    return out


def deserialize_json(data: dict) -> DashboardSummary:
    out: DashboardSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DashboardSummary.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DashboardSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "creationDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["creation_date"] = aws_sdk_iotsitewise.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    if "lastUpdateDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["last_update_date"] = aws_sdk_iotsitewise.types.timestamp.deserialize_json(
            data["lastUpdateDate"]
        )
    return out
