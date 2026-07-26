"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceReferenceChanges``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.service_reference_list


class ServiceReferenceChanges(TypedDict, closed=True):
    added: NotRequired[
        "capo_resiliencehubv2.types.service_reference_list.ServiceReferenceList"
    ]
    """<p>The list of service references that were added.</p>"""
    removed: NotRequired[
        "capo_resiliencehubv2.types.service_reference_list.ServiceReferenceList"
    ]
    """<p>The list of service references that were removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceReferenceChanges) -> dict:
    out: dict = {}
    if "added" in value:
        import capo_resiliencehubv2.types.service_reference_list

        out["added"] = capo_resiliencehubv2.types.service_reference_list.serialize_json(
            value["added"]
        )
    if "removed" in value:
        import capo_resiliencehubv2.types.service_reference_list

        out["removed"] = (
            capo_resiliencehubv2.types.service_reference_list.serialize_json(
                value["removed"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceReferenceChanges:
    out: ServiceReferenceChanges = {}  # type: ignore[typeddict-item]
    if "added" in data:
        import capo_resiliencehubv2.types.service_reference_list

        out["added"] = (
            capo_resiliencehubv2.types.service_reference_list.deserialize_json(
                data["added"]
            )
        )
    if "removed" in data:
        import capo_resiliencehubv2.types.service_reference_list

        out["removed"] = (
            capo_resiliencehubv2.types.service_reference_list.deserialize_json(
                data["removed"]
            )
        )
    return out
