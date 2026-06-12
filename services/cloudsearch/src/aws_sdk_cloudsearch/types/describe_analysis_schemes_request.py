"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DescribeAnalysisSchemesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.boolean
    import aws_sdk_cloudsearch.types.domain_name
    import aws_sdk_cloudsearch.types.standard_name_list


class DescribeAnalysisSchemesRequest(TypedDict):
    domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName"
    """<p>The name of the domain you want to describe.</p>"""
    analysis_scheme_names: NotRequired[
        "aws_sdk_cloudsearch.types.standard_name_list.StandardNameList"
    ]
    """<p>The analysis schemes you want to describe.</p>"""
    deployed: NotRequired["aws_sdk_cloudsearch.types.boolean.Boolean"]
    """<p>Whether to display the deployed configuration (<code>true</code>) or include any pending changes (<code>false</code>). Defaults to <code>false</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAnalysisSchemesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.DomainName", str(value["domain_name"])))
    if "analysis_scheme_names" in value:
        import aws_sdk_cloudsearch.types.standard_name_list

        aws_sdk_cloudsearch.types.standard_name_list.serialize_query(
            value["analysis_scheme_names"], pairs, f"{prefix}.AnalysisSchemeNames"
        )
    if "deployed" in value:
        pairs.append((f"{prefix}.Deployed", "true" if value["deployed"] else "false"))


def deserialize_query(el: Element) -> DescribeAnalysisSchemesRequest:
    out: DescribeAnalysisSchemesRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        raise DeserializationError(
            "DescribeAnalysisSchemesRequest.domain_name required"
        )
    child_analysis_scheme_names = el.find("AnalysisSchemeNames")
    if child_analysis_scheme_names is not None:
        import aws_sdk_cloudsearch.types.standard_name_list

        out["analysis_scheme_names"] = (
            aws_sdk_cloudsearch.types.standard_name_list.deserialize_query(
                child_analysis_scheme_names
            )
        )
    child_deployed = el.find("Deployed")
    if child_deployed is not None:
        out["deployed"] = (child_deployed.text or "").lower() == "true"
    return out
