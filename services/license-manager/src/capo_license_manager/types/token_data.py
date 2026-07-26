"""Generated from Smithy shape ``com.amazonaws.licensemanager#TokenData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.arn_list
    import capo_license_manager.types.iso8601_date_time
    import capo_license_manager.types.max_size3_string_list
    import capo_license_manager.types.string


class TokenData(TypedDict, closed=True):
    token_id: NotRequired["capo_license_manager.types.string.String"]
    """<p>Token ID.</p>"""
    token_type: NotRequired["capo_license_manager.types.string.String"]
    """<p>Type of token generated. The supported value is <code>REFRESH_TOKEN</code>.</p>"""
    license_arn: NotRequired["capo_license_manager.types.string.String"]
    """<p>Amazon Resource Name (ARN) of the license.</p>"""
    expiration_time: NotRequired[
        "capo_license_manager.types.iso8601_date_time.ISO8601DateTime"
    ]
    """<p>Token expiration time, in ISO8601-UTC format.</p>"""
    token_properties: NotRequired[
        "capo_license_manager.types.max_size3_string_list.MaxSize3StringList"
    ]
    """<p>Data specified by the caller.</p>"""
    role_arns: NotRequired["capo_license_manager.types.arn_list.ArnList"]
    """<p>Amazon Resource Names (ARN) of the roles included in the token.</p>"""
    status: NotRequired["capo_license_manager.types.string.String"]
    """<p>Token status. The possible values are <code>AVAILABLE</code> and <code>DELETED</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TokenData) -> dict:
    out: dict = {}
    if "token_id" in value:
        out["TokenId"] = value["token_id"]
    if "token_type" in value:
        out["TokenType"] = value["token_type"]
    if "license_arn" in value:
        out["LicenseArn"] = value["license_arn"]
    if "expiration_time" in value:
        out["ExpirationTime"] = value["expiration_time"]
    if "token_properties" in value:
        import capo_license_manager.types.max_size3_string_list

        out["TokenProperties"] = (
            capo_license_manager.types.max_size3_string_list.serialize_aws_json_1_1(
                value["token_properties"]
            )
        )
    if "role_arns" in value:
        import capo_license_manager.types.arn_list

        out["RoleArns"] = capo_license_manager.types.arn_list.serialize_aws_json_1_1(
            value["role_arns"]
        )
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TokenData:
    out: TokenData = {}  # type: ignore[typeddict-item]
    if "TokenId" in data:
        out["token_id"] = data["TokenId"]
    if "TokenType" in data:
        out["token_type"] = data["TokenType"]
    if "LicenseArn" in data:
        out["license_arn"] = data["LicenseArn"]
    if "ExpirationTime" in data:
        out["expiration_time"] = data["ExpirationTime"]
    if "TokenProperties" in data:
        import capo_license_manager.types.max_size3_string_list

        out["token_properties"] = (
            capo_license_manager.types.max_size3_string_list.deserialize_aws_json_1_1(
                data["TokenProperties"]
            )
        )
    if "RoleArns" in data:
        import capo_license_manager.types.arn_list

        out["role_arns"] = capo_license_manager.types.arn_list.deserialize_aws_json_1_1(
            data["RoleArns"]
        )
    if "Status" in data:
        out["status"] = data["Status"]
    return out
