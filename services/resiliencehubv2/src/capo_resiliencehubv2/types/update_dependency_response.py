"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdateDependencyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.dependency_criticality
    import capo_resiliencehubv2.types.uuid


class UpdateDependencyResponse(TypedDict, closed=True):
    dependency_id: "capo_resiliencehubv2.types.uuid.Uuid"
    """<p>The identifier of the updated dependency.</p>"""
    dependency_name: "str"
    """<p>The name of the updated dependency.</p>"""
    location: "str"
    """<p>The location of the dependency.</p>"""
    criticality: (
        "capo_resiliencehubv2.types.dependency_criticality.DependencyCriticality"
    )
    """<p>The criticality level of the dependency.</p>"""
    comment: NotRequired["str"]
    """<p>The comment about the dependency.</p>"""
    provider: NotRequired["str"]
    """<p>The provider of the dependency.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the dependency was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDependencyResponse) -> dict:
    out: dict = {}
    out["dependencyId"] = value["dependency_id"]
    out["dependencyName"] = value["dependency_name"]
    out["location"] = value["location"]
    import capo_resiliencehubv2.types.dependency_criticality

    out["criticality"] = (
        capo_resiliencehubv2.types.dependency_criticality.serialize_json(
            value["criticality"]
        )
    )
    if "comment" in value:
        out["comment"] = value["comment"]
    if "provider" in value:
        out["provider"] = value["provider"]
    import capo_resiliencehubv2.types._prelude.timestamp

    out["updatedAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDependencyResponse:
    out: UpdateDependencyResponse = {}  # type: ignore[typeddict-item]
    if "dependencyId" in data:
        out["dependency_id"] = data["dependencyId"]
    else:
        raise DeserializationError("UpdateDependencyResponse.dependency_id required")
    if "dependencyName" in data:
        out["dependency_name"] = data["dependencyName"]
    else:
        raise DeserializationError("UpdateDependencyResponse.dependency_name required")
    if "location" in data:
        out["location"] = data["location"]
    else:
        raise DeserializationError("UpdateDependencyResponse.location required")
    if "criticality" in data:
        import capo_resiliencehubv2.types.dependency_criticality

        out["criticality"] = (
            capo_resiliencehubv2.types.dependency_criticality.deserialize_json(
                data["criticality"]
            )
        )
    else:
        raise DeserializationError("UpdateDependencyResponse.criticality required")
    if "comment" in data:
        out["comment"] = data["comment"]
    if "provider" in data:
        out["provider"] = data["provider"]
    if "updatedAt" in data:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updated_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("UpdateDependencyResponse.updated_at required")
    return out
