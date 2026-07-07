"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListTypeRegistrationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.registration_token_list


class ListTypeRegistrationsOutput(TypedDict, closed=True):
    registration_token_list: NotRequired[
        "aws_sdk_cloudformation.types.registration_token_list.RegistrationTokenList"
    ]
    """<p>A list of extension registration tokens.</p> <p>Use <a>DescribeTypeRegistration</a> to return detailed information about a type registration request.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>If the request doesn't return all the remaining results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If the request returns all results, <code>NextToken</code> is set to <code>null</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListTypeRegistrationsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "registration_token_list" in value:
        import aws_sdk_cloudformation.types.registration_token_list

        aws_sdk_cloudformation.types.registration_token_list.serialize_query(
            value["registration_token_list"], pairs, f"{prefix}.RegistrationTokenList"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListTypeRegistrationsOutput:
    out: ListTypeRegistrationsOutput = {}  # type: ignore[typeddict-item]
    child_registration_token_list = el.find("RegistrationTokenList")
    if child_registration_token_list is not None:
        import aws_sdk_cloudformation.types.registration_token_list

        out["registration_token_list"] = (
            aws_sdk_cloudformation.types.registration_token_list.deserialize_query(
                child_registration_token_list
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
