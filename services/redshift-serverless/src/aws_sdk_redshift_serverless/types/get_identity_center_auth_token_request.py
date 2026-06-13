"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetIdentityCenterAuthTokenRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.workgroup_name_list


class GetIdentityCenterAuthTokenRequest(TypedDict):
    workgroup_names: (
        "aws_sdk_redshift_serverless.types.workgroup_name_list.WorkgroupNameList"
    )
    """<p>A list of workgroup names for which to generate the Identity Center authentication token.</p> <p>Constraints:</p> <ul> <li> <p>Must contain between 1 and 20 workgroup names.</p> </li> <li> <p>Each workgroup name must be a valid Amazon Redshift Serverless workgroup identifier.</p> </li> <li> <p>All specified workgroups must have Identity Center integration enabled.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetIdentityCenterAuthTokenRequest) -> dict:
    out: dict = {}
    import aws_sdk_redshift_serverless.types.workgroup_name_list

    out["workgroupNames"] = (
        aws_sdk_redshift_serverless.types.workgroup_name_list.serialize_aws_json_1_1(
            value["workgroup_names"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetIdentityCenterAuthTokenRequest:
    out: GetIdentityCenterAuthTokenRequest = {}  # type: ignore[typeddict-item]
    if "workgroupNames" in data:
        import aws_sdk_redshift_serverless.types.workgroup_name_list

        out["workgroup_names"] = (
            aws_sdk_redshift_serverless.types.workgroup_name_list.deserialize_aws_json_1_1(
                data["workgroupNames"]
            )
        )
    else:
        raise DeserializationError(
            "GetIdentityCenterAuthTokenRequest.workgroup_names required"
        )
    return out
