"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#TemplateRevision``."""

from typing_extensions import TypedDict

from capo_pca_connector_ad.errors import DeserializationError


class TemplateRevision(TypedDict, closed=True):
    major_revision: "int"
    """<p>The revision version of the template. Re-enrolling all certificate holders will increment the major revision.</p>"""
    minor_revision: "int"
    """<p>The revision version of the template. Re-enrolling all certificate holders will increment the major revision.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateRevision) -> dict:
    out: dict = {}
    out["MajorRevision"] = value["major_revision"]
    out["MinorRevision"] = value["minor_revision"]
    return out


def deserialize_json(data: dict) -> TemplateRevision:
    out: TemplateRevision = {}  # type: ignore[typeddict-item]
    if "MajorRevision" in data:
        out["major_revision"] = data["MajorRevision"]
    else:
        raise DeserializationError("TemplateRevision.major_revision required")
    if "MinorRevision" in data:
        out["minor_revision"] = data["MinorRevision"]
    else:
        raise DeserializationError("TemplateRevision.minor_revision required")
    return out
