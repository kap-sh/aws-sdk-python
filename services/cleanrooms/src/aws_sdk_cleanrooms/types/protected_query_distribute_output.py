"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryDistributeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.protected_query_member_output_list
    import aws_sdk_cleanrooms.types.protected_query_s3_output


class ProtectedQueryDistributeOutput(TypedDict, closed=True):
    s3: NotRequired[
        "aws_sdk_cleanrooms.types.protected_query_s3_output.ProtectedQueryS3Output"
    ]
    member_list: NotRequired[
        "aws_sdk_cleanrooms.types.protected_query_member_output_list.ProtectedQueryMemberOutputList"
    ]
    """<p> Contains the output results for each member location specified in the distribute output configuration. Each entry provides details about the result distribution to a specific collaboration member. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryDistributeOutput) -> dict:
    out: dict = {}
    if "s3" in value:
        import aws_sdk_cleanrooms.types.protected_query_s3_output

        out["s3"] = aws_sdk_cleanrooms.types.protected_query_s3_output.serialize_json(
            value["s3"]
        )
    if "member_list" in value:
        import aws_sdk_cleanrooms.types.protected_query_member_output_list

        out["memberList"] = (
            aws_sdk_cleanrooms.types.protected_query_member_output_list.serialize_json(
                value["member_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProtectedQueryDistributeOutput:
    out: ProtectedQueryDistributeOutput = {}  # type: ignore[typeddict-item]
    if "s3" in data:
        import aws_sdk_cleanrooms.types.protected_query_s3_output

        out["s3"] = aws_sdk_cleanrooms.types.protected_query_s3_output.deserialize_json(
            data["s3"]
        )
    if "memberList" in data:
        import aws_sdk_cleanrooms.types.protected_query_member_output_list

        out["member_list"] = (
            aws_sdk_cleanrooms.types.protected_query_member_output_list.deserialize_json(
                data["memberList"]
            )
        )
    return out
