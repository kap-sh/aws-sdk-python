"""Generated from Smithy shape ``com.amazonaws.inspector#ListRulesPackagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector.types.list_returned_arn_list
    import capo_inspector.types.pagination_token


class ListRulesPackagesResponse(TypedDict, closed=True):
    rules_package_arns: (
        "capo_inspector.types.list_returned_arn_list.ListReturnedArnList"
    )
    """<p>The list of ARNs that specifies the rules packages returned by the action.</p>"""
    next_token: NotRequired["capo_inspector.types.pagination_token.PaginationToken"]
    """<p> When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the <b>nextToken</b> parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRulesPackagesResponse) -> dict:
    out: dict = {}
    import capo_inspector.types.list_returned_arn_list

    out["rulesPackageArns"] = (
        capo_inspector.types.list_returned_arn_list.serialize_aws_json_1_1(
            value["rules_package_arns"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRulesPackagesResponse:
    out: ListRulesPackagesResponse = {}  # type: ignore[typeddict-item]
    if "rulesPackageArns" in data:
        import capo_inspector.types.list_returned_arn_list

        out["rules_package_arns"] = (
            capo_inspector.types.list_returned_arn_list.deserialize_aws_json_1_1(
                data["rulesPackageArns"]
            )
        )
    else:
        raise DeserializationError(
            "ListRulesPackagesResponse.rules_package_arns required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
