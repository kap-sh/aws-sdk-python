"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeOrganizationOverviewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.account_id_list
    import aws_sdk_devops_guru.types.organizational_unit_id_list
    import aws_sdk_devops_guru.types.timestamp


class DescribeOrganizationOverviewRequest(TypedDict, closed=True):
    from_time: "aws_sdk_devops_guru.types.timestamp.Timestamp"
    """<p> The start of the time range passed in. The start time granularity is at the day level. The floor of the start time is used. Returned information occurred after this day. </p>"""
    to_time: NotRequired["aws_sdk_devops_guru.types.timestamp.Timestamp"]
    """<p> The end of the time range passed in. The start time granularity is at the day level. The floor of the start time is used. Returned information occurred before this day. If this is not specified, then the current day is used. </p>"""
    account_ids: NotRequired["aws_sdk_devops_guru.types.account_id_list.AccountIdList"]
    """<p>The ID of the Amazon Web Services account.</p>"""
    organizational_unit_ids: NotRequired[
        "aws_sdk_devops_guru.types.organizational_unit_id_list.OrganizationalUnitIdList"
    ]
    """<p>The ID of the organizational unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOrganizationOverviewRequest) -> dict:
    out: dict = {}
    import aws_sdk_devops_guru.types.timestamp

    out["FromTime"] = aws_sdk_devops_guru.types.timestamp.serialize_json(
        value["from_time"]
    )
    if "to_time" in value:
        import aws_sdk_devops_guru.types.timestamp

        out["ToTime"] = aws_sdk_devops_guru.types.timestamp.serialize_json(
            value["to_time"]
        )
    if "account_ids" in value:
        import aws_sdk_devops_guru.types.account_id_list

        out["AccountIds"] = aws_sdk_devops_guru.types.account_id_list.serialize_json(
            value["account_ids"]
        )
    if "organizational_unit_ids" in value:
        import aws_sdk_devops_guru.types.organizational_unit_id_list

        out["OrganizationalUnitIds"] = (
            aws_sdk_devops_guru.types.organizational_unit_id_list.serialize_json(
                value["organizational_unit_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeOrganizationOverviewRequest:
    out: DescribeOrganizationOverviewRequest = {}  # type: ignore[typeddict-item]
    if "FromTime" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["from_time"] = aws_sdk_devops_guru.types.timestamp.deserialize_json(
            data["FromTime"]
        )
    else:
        raise DeserializationError(
            "DescribeOrganizationOverviewRequest.from_time required"
        )
    if "ToTime" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["to_time"] = aws_sdk_devops_guru.types.timestamp.deserialize_json(
            data["ToTime"]
        )
    if "AccountIds" in data:
        import aws_sdk_devops_guru.types.account_id_list

        out["account_ids"] = aws_sdk_devops_guru.types.account_id_list.deserialize_json(
            data["AccountIds"]
        )
    if "OrganizationalUnitIds" in data:
        import aws_sdk_devops_guru.types.organizational_unit_id_list

        out["organizational_unit_ids"] = (
            aws_sdk_devops_guru.types.organizational_unit_id_list.deserialize_json(
                data["OrganizationalUnitIds"]
            )
        )
    return out
