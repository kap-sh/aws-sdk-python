"""Generated from Smithy shape ``com.amazonaws.securityhub#Severity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.double
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.severity_label


class Severity(TypedDict):
    product: NotRequired["aws_sdk_securityhub.types.double.Double"]
    """<p>Deprecated. This attribute isn't included in findings. Instead of providing <code>Product</code>, provide <code>Original</code>.</p> <p>The native severity as defined by the Amazon Web Services service or integrated partner product that generated the finding.</p>"""
    label: NotRequired["aws_sdk_securityhub.types.severity_label.SeverityLabel"]
    """<p>The severity value of the finding. The allowed values are the following.</p> <ul> <li> <p> <code>INFORMATIONAL</code> - No issue was found.</p> </li> <li> <p> <code>LOW</code> - The issue does not require action on its own.</p> </li> <li> <p> <code>MEDIUM</code> - The issue must be addressed but not urgently.</p> </li> <li> <p> <code>HIGH</code> - The issue must be addressed as a priority.</p> </li> <li> <p> <code>CRITICAL</code> - The issue must be remediated immediately to avoid it escalating.</p> </li> </ul> <p>If you provide <code>Normalized</code> and don't provide <code>Label</code>, then <code>Label</code> is set automatically as follows. </p> <ul> <li> <p>0 - <code>INFORMATIONAL</code> </p> </li> <li> <p>1–39 - <code>LOW</code> </p> </li> <li> <p>40–69 - <code>MEDIUM</code> </p> </li> <li> <p>70–89 - <code>HIGH</code> </p> </li> <li> <p>90–100 - <code>CRITICAL</code> </p> </li> </ul>"""
    normalized: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>Deprecated. The normalized severity of a finding. Instead of providing <code>Normalized</code>, provide <code>Label</code>.</p> <p>The value of <code>Normalized</code> can be an integer between <code>0</code> and <code>100</code>.</p> <p>If you provide <code>Label</code> and don't provide <code>Normalized</code>, then <code>Normalized</code> is set automatically as follows.</p> <ul> <li> <p> <code>INFORMATIONAL</code> - 0</p> </li> <li> <p> <code>LOW</code> - 1</p> </li> <li> <p> <code>MEDIUM</code> - 40</p> </li> <li> <p> <code>HIGH</code> - 70</p> </li> <li> <p> <code>CRITICAL</code> - 90</p> </li> </ul>"""
    original: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The native severity from the finding product that generated the finding.</p> <p>Length Constraints: Minimum length of 1. Maximum length of 64.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Severity) -> dict:
    out: dict = {}
    if "product" in value:
        out["Product"] = value["product"]
    if "label" in value:
        import aws_sdk_securityhub.types.severity_label

        out["Label"] = aws_sdk_securityhub.types.severity_label.serialize_json(
            value["label"]
        )
    if "normalized" in value:
        out["Normalized"] = value["normalized"]
    if "original" in value:
        out["Original"] = value["original"]
    return out


def deserialize_json(data: dict) -> Severity:
    out: Severity = {}  # type: ignore[typeddict-item]
    if "Product" in data:
        out["product"] = data["Product"]
    if "Label" in data:
        import aws_sdk_securityhub.types.severity_label

        out["label"] = aws_sdk_securityhub.types.severity_label.deserialize_json(
            data["Label"]
        )
    if "Normalized" in data:
        out["normalized"] = data["Normalized"]
    if "Original" in data:
        out["original"] = data["Original"]
    return out
