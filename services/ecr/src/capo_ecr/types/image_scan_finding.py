"""Generated from Smithy shape ``com.amazonaws.ecr#ImageScanFinding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.attribute_list
    import capo_ecr.types.finding_description
    import capo_ecr.types.finding_name
    import capo_ecr.types.finding_severity
    import capo_ecr.types.url


class ImageScanFinding(TypedDict, closed=True):
    name: NotRequired["capo_ecr.types.finding_name.FindingName"]
    """<p>The name associated with the finding, usually a CVE number.</p>"""
    description: NotRequired["capo_ecr.types.finding_description.FindingDescription"]
    """<p>The description of the finding.</p>"""
    uri: NotRequired["capo_ecr.types.url.Url"]
    """<p>A link containing additional details about the security vulnerability.</p>"""
    severity: NotRequired["capo_ecr.types.finding_severity.FindingSeverity"]
    """<p>The finding severity.</p>"""
    attributes: NotRequired["capo_ecr.types.attribute_list.AttributeList"]
    """<p>A collection of attributes of the host from which the finding is generated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageScanFinding) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "uri" in value:
        out["uri"] = value["uri"]
    if "severity" in value:
        import capo_ecr.types.finding_severity

        out["severity"] = capo_ecr.types.finding_severity.serialize_aws_json_1_1(
            value["severity"]
        )
    if "attributes" in value:
        import capo_ecr.types.attribute_list

        out["attributes"] = capo_ecr.types.attribute_list.serialize_aws_json_1_1(
            value["attributes"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageScanFinding:
    out: ImageScanFinding = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    if data.get("severity") is not None:
        import capo_ecr.types.finding_severity

        out["severity"] = capo_ecr.types.finding_severity.deserialize_aws_json_1_1(
            data["severity"]
        )
    if data.get("attributes") is not None:
        import capo_ecr.types.attribute_list

        out["attributes"] = capo_ecr.types.attribute_list.deserialize_aws_json_1_1(
            data["attributes"]
        )
    return out
