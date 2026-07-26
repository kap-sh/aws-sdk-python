"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DomainObjectTypeField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.content_type
    import capo_customer_profiles.types.feature_type
    import capo_customer_profiles.types.text


class DomainObjectTypeField(TypedDict, closed=True):
    source: "capo_customer_profiles.types.text.text"
    """<p>The expression that defines how to extract the field value from the source object.></p>"""
    target: "capo_customer_profiles.types.text.text"
    """<p>The expression that defines where the field value should be placed in the standard domain object.</p>"""
    content_type: NotRequired["capo_customer_profiles.types.content_type.ContentType"]
    """<p>The content type of the field.</p>"""
    feature_type: NotRequired["capo_customer_profiles.types.feature_type.FeatureType"]
    """<p>The semantic meaning of the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainObjectTypeField) -> dict:
    out: dict = {}
    out["Source"] = value["source"]
    out["Target"] = value["target"]
    if "content_type" in value:
        import capo_customer_profiles.types.content_type

        out["ContentType"] = capo_customer_profiles.types.content_type.serialize_json(
            value["content_type"]
        )
    if "feature_type" in value:
        import capo_customer_profiles.types.feature_type

        out["FeatureType"] = capo_customer_profiles.types.feature_type.serialize_json(
            value["feature_type"]
        )
    return out


def deserialize_json(data: dict) -> DomainObjectTypeField:
    out: DomainObjectTypeField = {}  # type: ignore[typeddict-item]
    if "Source" in data:
        out["source"] = data["Source"]
    else:
        raise DeserializationError("DomainObjectTypeField.source required")
    if "Target" in data:
        out["target"] = data["Target"]
    else:
        raise DeserializationError("DomainObjectTypeField.target required")
    if "ContentType" in data:
        import capo_customer_profiles.types.content_type

        out["content_type"] = (
            capo_customer_profiles.types.content_type.deserialize_json(
                data["ContentType"]
            )
        )
    if "FeatureType" in data:
        import capo_customer_profiles.types.feature_type

        out["feature_type"] = (
            capo_customer_profiles.types.feature_type.deserialize_json(
                data["FeatureType"]
            )
        )
    return out
