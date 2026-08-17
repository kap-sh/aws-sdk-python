"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeAvailablePatchesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.next_token
    import capo_ssm.types.patch_baseline_max_results
    import capo_ssm.types.patch_orchestrator_filter_list


class DescribeAvailablePatchesRequest(TypedDict, closed=True):
    filters: NotRequired[
        "capo_ssm.types.patch_orchestrator_filter_list.PatchOrchestratorFilterList"
    ]
    """<p>Each element in the array is a structure containing a key-value pair.</p> <p> <b>Windows Server</b> </p> <p>Supported keys for Windows Server managed node patches include the following:</p> <ul> <li> <p> <b> <code>PATCH_SET</code> </b> </p> <p>Sample values: <code>OS</code> | <code>APPLICATION</code> </p> </li> <li> <p> <b> <code>PRODUCT</code> </b> </p> <p>Sample values: <code>WindowsServer2012</code> | <code>Office 2010</code> | <code>MicrosoftDefenderAntivirus</code> </p> </li> <li> <p> <b> <code>PRODUCT_FAMILY</code> </b> </p> <p>Sample values: <code>Windows</code> | <code>Office</code> </p> </li> <li> <p> <b> <code>MSRC_SEVERITY</code> </b> </p> <p>Sample values: <code>ServicePacks</code> | <code>Important</code> | <code>Moderate</code> </p> </li> <li> <p> <b> <code>CLASSIFICATION</code> </b> </p> <p>Sample values: <code>ServicePacks</code> | <code>SecurityUpdates</code> | <code>DefinitionUpdates</code> </p> </li> <li> <p> <b> <code>PATCH_ID</code> </b> </p> <p>Sample values: <code>KB123456</code> | <code>KB4516046</code> </p> </li> </ul> <p> <b>Linux</b> </p> <important> <p>When specifying filters for Linux patches, you must specify a key-pair for <code>PRODUCT</code>. For example, using the Command Line Interface (CLI), the following command fails:</p> <p> <code>aws ssm describe-available-patches --filters Key=CVE_ID,Values=CVE-2018-3615</code> </p> <p>However, the following command succeeds:</p> <p> <code>aws ssm describe-available-patches --filters Key=PRODUCT,Values=AmazonLinux2018.03 Key=CVE_ID,Values=CVE-2018-3615</code> </p> </important> <p>Supported keys for Linux managed node patches include the following:</p> <ul> <li> <p> <b> <code>PRODUCT</code> </b> </p> <p>Sample values: <code>AmazonLinux2018.03</code> | <code>AmazonLinux2.0</code> </p> </li> <li> <p> <b> <code>NAME</code> </b> </p> <p>Sample values: <code>kernel-headers</code> | <code>samba-python</code> | <code>php</code> </p> </li> <li> <p> <b> <code>SEVERITY</code> </b> </p> <p>Sample values: <code>Critical</code> | <code>Important</code> | <code>Medium</code> | <code>Low</code> </p> </li> <li> <p> <b> <code>EPOCH</code> </b> </p> <p>Sample values: <code>0</code> | <code>1</code> </p> </li> <li> <p> <b> <code>VERSION</code> </b> </p> <p>Sample values: <code>78.6.1</code> | <code>4.10.16</code> </p> </li> <li> <p> <b> <code>RELEASE</code> </b> </p> <p>Sample values: <code>9.56.amzn1</code> | <code>1.amzn2</code> </p> </li> <li> <p> <b> <code>ARCH</code> </b> </p> <p>Sample values: <code>i686</code> | <code>x86_64</code> </p> </li> <li> <p> <b> <code>REPOSITORY</code> </b> </p> <p>Sample values: <code>Core</code> | <code>Updates</code> </p> </li> <li> <p> <b> <code>ADVISORY_ID</code> </b> </p> <p>Sample values: <code>ALAS-2018-1058</code> | <code>ALAS2-2021-1594</code> </p> </li> <li> <p> <b> <code>CVE_ID</code> </b> </p> <p>Sample values: <code>CVE-2018-3615</code> | <code>CVE-2020-1472</code> </p> </li> <li> <p> <b> <code>BUGZILLA_ID</code> </b> </p> <p>Sample values: <code>1463241</code> </p> </li> </ul>"""
    max_results: NotRequired[
        "capo_ssm.types.patch_baseline_max_results.PatchBaselineMaxResults"
    ]
    """<p>The maximum number of patches to return (per page).</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAvailablePatchesRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_ssm.types.patch_orchestrator_filter_list

        out["Filters"] = (
            capo_ssm.types.patch_orchestrator_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAvailablePatchesRequest:
    out: DescribeAvailablePatchesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_ssm.types.patch_orchestrator_filter_list

        out["filters"] = (
            capo_ssm.types.patch_orchestrator_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
