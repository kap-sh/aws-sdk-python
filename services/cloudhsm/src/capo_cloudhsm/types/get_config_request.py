"""Generated from Smithy shape ``com.amazonaws.cloudhsm#GetConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudhsm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudhsm.types.client_arn
    import capo_cloudhsm.types.client_version
    import capo_cloudhsm.types.hapg_list


class GetConfigRequest(TypedDict, closed=True):
    client_arn: "capo_cloudhsm.types.client_arn.ClientArn"
    """<p>The ARN of the client.</p>"""
    client_version: "capo_cloudhsm.types.client_version.ClientVersion"
    """<p>The client version.</p>"""
    hapg_list: "capo_cloudhsm.types.hapg_list.HapgList"
    """<p>A list of ARNs that identify the high-availability partition groups that are associated with the client.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetConfigRequest) -> dict:
    out: dict = {}
    out["ClientArn"] = value["client_arn"]
    import capo_cloudhsm.types.client_version

    out["ClientVersion"] = capo_cloudhsm.types.client_version.serialize_aws_json_1_1(
        value["client_version"]
    )
    import capo_cloudhsm.types.hapg_list

    out["HapgList"] = capo_cloudhsm.types.hapg_list.serialize_aws_json_1_1(
        value["hapg_list"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetConfigRequest:
    out: GetConfigRequest = {}  # type: ignore[typeddict-item]
    if "ClientArn" in data:
        out["client_arn"] = data["ClientArn"]
    else:
        raise DeserializationError("GetConfigRequest.client_arn required")
    if "ClientVersion" in data:
        import capo_cloudhsm.types.client_version

        out["client_version"] = (
            capo_cloudhsm.types.client_version.deserialize_aws_json_1_1(
                data["ClientVersion"]
            )
        )
    else:
        raise DeserializationError("GetConfigRequest.client_version required")
    if "HapgList" in data:
        import capo_cloudhsm.types.hapg_list

        out["hapg_list"] = capo_cloudhsm.types.hapg_list.deserialize_aws_json_1_1(
            data["HapgList"]
        )
    else:
        raise DeserializationError("GetConfigRequest.hapg_list required")
    return out
