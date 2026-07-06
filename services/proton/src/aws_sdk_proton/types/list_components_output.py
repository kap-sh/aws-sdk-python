"""Generated from Smithy shape ``com.amazonaws.proton#ListComponentsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.component_summary_list
    import aws_sdk_proton.types.next_token


class ListComponentsOutput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next component in the array of components, after the current requested list of components.</p>"""
    components: "aws_sdk_proton.types.component_summary_list.ComponentSummaryList"
    """<p>An array of components with summary data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListComponentsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_proton.types.component_summary_list

    out["components"] = (
        aws_sdk_proton.types.component_summary_list.serialize_aws_json_1_0(
            value["components"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListComponentsOutput:
    out: ListComponentsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "components" in data:
        import aws_sdk_proton.types.component_summary_list

        out["components"] = (
            aws_sdk_proton.types.component_summary_list.deserialize_aws_json_1_0(
                data["components"]
            )
        )
    else:
        raise DeserializationError("ListComponentsOutput.components required")
    return out
