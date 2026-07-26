"""Generated from Smithy shape ``com.amazonaws.securityhub#Cvss``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.adjustment_list
    import capo_securityhub.types.double
    import capo_securityhub.types.non_empty_string


class Cvss(TypedDict, closed=True):
    version: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The version of CVSS for the CVSS score.</p>"""
    base_score: NotRequired["capo_securityhub.types.double.Double"]
    """<p>The base CVSS score.</p>"""
    base_vector: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The base scoring vector for the CVSS score.</p>"""
    source: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The origin of the original CVSS score and vector.</p>"""
    adjustments: NotRequired["capo_securityhub.types.adjustment_list.AdjustmentList"]
    """<p>Adjustments to the CVSS metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Cvss) -> dict:
    out: dict = {}
    if "version" in value:
        out["Version"] = value["version"]
    if "base_score" in value:
        out["BaseScore"] = value["base_score"]
    if "base_vector" in value:
        out["BaseVector"] = value["base_vector"]
    if "source" in value:
        out["Source"] = value["source"]
    if "adjustments" in value:
        import capo_securityhub.types.adjustment_list

        out["Adjustments"] = capo_securityhub.types.adjustment_list.serialize_json(
            value["adjustments"]
        )
    return out


def deserialize_json(data: dict) -> Cvss:
    out: Cvss = {}  # type: ignore[typeddict-item]
    if "Version" in data:
        out["version"] = data["Version"]
    if "BaseScore" in data:
        out["base_score"] = data["BaseScore"]
    if "BaseVector" in data:
        out["base_vector"] = data["BaseVector"]
    if "Source" in data:
        out["source"] = data["Source"]
    if "Adjustments" in data:
        import capo_securityhub.types.adjustment_list

        out["adjustments"] = capo_securityhub.types.adjustment_list.deserialize_json(
            data["Adjustments"]
        )
    return out
