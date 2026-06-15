"""Generated from Smithy shape ``com.amazonaws.iam#GetContextKeysForCustomPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.simulation_policy_list_type


class GetContextKeysForCustomPolicyRequest(TypedDict):
    policy_input_list: (
        "aws_sdk_iam.types.simulation_policy_list_type.SimulationPolicyListType"
    )
    r"""<p>A list of policies for which you want the list of context keys referenced in those policies. Each document is specified as a string containing the complete, valid JSON text of an IAM policy.</p> <p>The <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a> used to validate this parameter is a string of characters consisting of the following:</p> <ul> <li> <p>Any printable ASCII character ranging from the space character (<code>\u0020</code>) through the end of the ASCII character range</p> </li> <li> <p>The printable characters in the Basic Latin and Latin-1 Supplement character set (through <code>\u00FF</code>)</p> </li> <li> <p>The special characters tab (<code>\u0009</code>), line feed (<code>\u000A</code>), and carriage return (<code>\u000D</code>)</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetContextKeysForCustomPolicyRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import aws_sdk_iam.types.simulation_policy_list_type

    aws_sdk_iam.types.simulation_policy_list_type.serialize_query(
        value["policy_input_list"], pairs, f"{prefix}.PolicyInputList"
    )


def deserialize_query(el: Element) -> GetContextKeysForCustomPolicyRequest:
    out: GetContextKeysForCustomPolicyRequest = {}  # type: ignore[typeddict-item]
    child_policy_input_list = el.find("PolicyInputList")
    if child_policy_input_list is not None:
        import aws_sdk_iam.types.simulation_policy_list_type

        out["policy_input_list"] = (
            aws_sdk_iam.types.simulation_policy_list_type.deserialize_query(
                child_policy_input_list
            )
        )
    else:
        raise DeserializationError(
            "GetContextKeysForCustomPolicyRequest.policy_input_list required"
        )
    return out
