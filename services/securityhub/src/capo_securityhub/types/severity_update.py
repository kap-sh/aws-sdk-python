"""Generated from Smithy shape ``com.amazonaws.securityhub#SeverityUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.double
    import capo_securityhub.types.ratio_scale
    import capo_securityhub.types.severity_label


class SeverityUpdate(TypedDict, closed=True):
    normalized: NotRequired["capo_securityhub.types.ratio_scale.RatioScale"]
    """<p>The normalized severity for the finding. This attribute is to be deprecated in favor of <code>Label</code>.</p> <p>If you provide <code>Normalized</code> and don't provide <code>Label</code>, <code>Label</code> is set automatically as follows.</p> <ul> <li> <p>0 - <code>INFORMATIONAL</code> </p> </li> <li> <p>1–39 - <code>LOW</code> </p> </li> <li> <p>40–69 - <code>MEDIUM</code> </p> </li> <li> <p>70–89 - <code>HIGH</code> </p> </li> <li> <p>90–100 - <code>CRITICAL</code> </p> </li> </ul>"""
    product: NotRequired["capo_securityhub.types.double.Double"]
    """<p>The native severity as defined by the Amazon Web Services service or integrated partner product that generated the finding.</p>"""
    label: NotRequired["capo_securityhub.types.severity_label.SeverityLabel"]
    """<p>The severity value of the finding. The allowed values are the following.</p> <ul> <li> <p> <code>INFORMATIONAL</code> - No issue was found.</p> </li> <li> <p> <code>LOW</code> - The issue does not require action on its own.</p> </li> <li> <p> <code>MEDIUM</code> - The issue must be addressed but not urgently.</p> </li> <li> <p> <code>HIGH</code> - The issue must be addressed as a priority.</p> </li> <li> <p> <code>CRITICAL</code> - The issue must be remediated immediately to avoid it escalating.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: SeverityUpdate) -> dict:
    out: dict = {}
    if "normalized" in value:
        out["Normalized"] = value["normalized"]
    if "product" in value:
        out["Product"] = value["product"]
    if "label" in value:
        import capo_securityhub.types.severity_label

        out["Label"] = capo_securityhub.types.severity_label.serialize_json(
            value["label"]
        )
    return out


def deserialize_json(data: dict) -> SeverityUpdate:
    out: SeverityUpdate = {}  # type: ignore[typeddict-item]
    if "Normalized" in data:
        out["normalized"] = data["Normalized"]
    if "Product" in data:
        out["product"] = data["Product"]
    if "Label" in data:
        import capo_securityhub.types.severity_label

        out["label"] = capo_securityhub.types.severity_label.deserialize_json(
            data["Label"]
        )
    return out
