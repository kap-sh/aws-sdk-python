"""Generated from Smithy shape ``com.amazonaws.inspector2#SearchVulnerabilitiesFilterCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.vuln_id_list


class SearchVulnerabilitiesFilterCriteria(TypedDict):
    vulnerability_ids: "aws_sdk_inspector2.types.vuln_id_list.VulnIdList"
    """<p>The IDs for specific vulnerabilities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchVulnerabilitiesFilterCriteria) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.vuln_id_list

    out["vulnerabilityIds"] = aws_sdk_inspector2.types.vuln_id_list.serialize_json(
        value["vulnerability_ids"]
    )
    return out


def deserialize_json(data: dict) -> SearchVulnerabilitiesFilterCriteria:
    out: SearchVulnerabilitiesFilterCriteria = {}  # type: ignore[typeddict-item]
    if "vulnerabilityIds" in data:
        import aws_sdk_inspector2.types.vuln_id_list

        out["vulnerability_ids"] = (
            aws_sdk_inspector2.types.vuln_id_list.deserialize_json(
                data["vulnerabilityIds"]
            )
        )
    else:
        raise DeserializationError(
            "SearchVulnerabilitiesFilterCriteria.vulnerability_ids required"
        )
    return out
