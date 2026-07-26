"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListDomainItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.timestamp


class ListDomainItem(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    created_at: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>The timestamp of when the domain was created.</p>"""
    last_updated_at: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>The timestamp of when the domain was most recently edited.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainItem) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    import capo_customer_profiles.types.timestamp

    out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_customer_profiles.types.timestamp

    out["LastUpdatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["last_updated_at"]
    )
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListDomainItem:
    out: ListDomainItem = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("ListDomainItem.domain_name required")
    if "CreatedAt" in data:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("ListDomainItem.created_at required")
    if "LastUpdatedAt" in data:
        import capo_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError("ListDomainItem.last_updated_at required")
    if "Tags" in data:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
