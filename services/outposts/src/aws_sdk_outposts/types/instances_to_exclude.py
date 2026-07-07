"""Generated from Smithy shape ``com.amazonaws.outposts#InstancesToExclude``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.account_id_list
    import aws_sdk_outposts.types.aws_service_name_list
    import aws_sdk_outposts.types.instance_id_list


class InstancesToExclude(TypedDict, closed=True):
    instances: NotRequired["aws_sdk_outposts.types.instance_id_list.InstanceIdList"]
    """<p>List of user-specified instances that must not be stopped.</p>"""
    account_ids: NotRequired["aws_sdk_outposts.types.account_id_list.AccountIdList"]
    """<p>IDs of the accounts that own each instance that must not be stopped.</p>"""
    services: NotRequired[
        "aws_sdk_outposts.types.aws_service_name_list.AWSServiceNameList"
    ]
    """<p>Names of the services that own each instance that must not be stopped in order to free up the capacity needed to run the capacity task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstancesToExclude) -> dict:
    out: dict = {}
    if "instances" in value:
        import aws_sdk_outposts.types.instance_id_list

        out["Instances"] = aws_sdk_outposts.types.instance_id_list.serialize_json(
            value["instances"]
        )
    if "account_ids" in value:
        import aws_sdk_outposts.types.account_id_list

        out["AccountIds"] = aws_sdk_outposts.types.account_id_list.serialize_json(
            value["account_ids"]
        )
    if "services" in value:
        import aws_sdk_outposts.types.aws_service_name_list

        out["Services"] = aws_sdk_outposts.types.aws_service_name_list.serialize_json(
            value["services"]
        )
    return out


def deserialize_json(data: dict) -> InstancesToExclude:
    out: InstancesToExclude = {}  # type: ignore[typeddict-item]
    if "Instances" in data:
        import aws_sdk_outposts.types.instance_id_list

        out["instances"] = aws_sdk_outposts.types.instance_id_list.deserialize_json(
            data["Instances"]
        )
    if "AccountIds" in data:
        import aws_sdk_outposts.types.account_id_list

        out["account_ids"] = aws_sdk_outposts.types.account_id_list.deserialize_json(
            data["AccountIds"]
        )
    if "Services" in data:
        import aws_sdk_outposts.types.aws_service_name_list

        out["services"] = aws_sdk_outposts.types.aws_service_name_list.deserialize_json(
            data["Services"]
        )
    return out
