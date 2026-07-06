"""Generated from Smithy shape ``com.amazonaws.iot#MitigationActionParams``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.add_things_to_thing_group_params
    import aws_sdk_iot.types.enable_io_t_logging_params
    import aws_sdk_iot.types.publish_finding_to_sns_params
    import aws_sdk_iot.types.replace_default_policy_version_params
    import aws_sdk_iot.types.update_ca_certificate_params
    import aws_sdk_iot.types.update_device_certificate_params


class MitigationActionParams(TypedDict, closed=True):
    update_device_certificate_params: NotRequired[
        "aws_sdk_iot.types.update_device_certificate_params.UpdateDeviceCertificateParams"
    ]
    """<p>Parameters to define a mitigation action that changes the state of the device certificate to inactive.</p>"""
    update_ca_certificate_params: NotRequired[
        "aws_sdk_iot.types.update_ca_certificate_params.UpdateCACertificateParams"
    ]
    """<p>Parameters to define a mitigation action that changes the state of the CA certificate to inactive.</p>"""
    add_things_to_thing_group_params: NotRequired[
        "aws_sdk_iot.types.add_things_to_thing_group_params.AddThingsToThingGroupParams"
    ]
    """<p>Parameters to define a mitigation action that moves devices associated with a certificate to one or more specified thing groups, typically for quarantine.</p>"""
    replace_default_policy_version_params: NotRequired[
        "aws_sdk_iot.types.replace_default_policy_version_params.ReplaceDefaultPolicyVersionParams"
    ]
    """<p>Parameters to define a mitigation action that adds a blank policy to restrict permissions.</p>"""
    enable_io_t_logging_params: NotRequired[
        "aws_sdk_iot.types.enable_io_t_logging_params.EnableIoTLoggingParams"
    ]
    """<p>Parameters to define a mitigation action that enables Amazon Web Services IoT Core logging at a specified level of detail.</p>"""
    publish_finding_to_sns_params: NotRequired[
        "aws_sdk_iot.types.publish_finding_to_sns_params.PublishFindingToSnsParams"
    ]
    """<p>Parameters to define a mitigation action that publishes findings to Amazon Simple Notification Service (Amazon SNS. You can implement your own custom actions in response to the Amazon SNS messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MitigationActionParams) -> dict:
    out: dict = {}
    if "update_device_certificate_params" in value:
        import aws_sdk_iot.types.update_device_certificate_params

        out["updateDeviceCertificateParams"] = (
            aws_sdk_iot.types.update_device_certificate_params.serialize_json(
                value["update_device_certificate_params"]
            )
        )
    if "update_ca_certificate_params" in value:
        import aws_sdk_iot.types.update_ca_certificate_params

        out["updateCACertificateParams"] = (
            aws_sdk_iot.types.update_ca_certificate_params.serialize_json(
                value["update_ca_certificate_params"]
            )
        )
    if "add_things_to_thing_group_params" in value:
        import aws_sdk_iot.types.add_things_to_thing_group_params

        out["addThingsToThingGroupParams"] = (
            aws_sdk_iot.types.add_things_to_thing_group_params.serialize_json(
                value["add_things_to_thing_group_params"]
            )
        )
    if "replace_default_policy_version_params" in value:
        import aws_sdk_iot.types.replace_default_policy_version_params

        out["replaceDefaultPolicyVersionParams"] = (
            aws_sdk_iot.types.replace_default_policy_version_params.serialize_json(
                value["replace_default_policy_version_params"]
            )
        )
    if "enable_io_t_logging_params" in value:
        import aws_sdk_iot.types.enable_io_t_logging_params

        out["enableIoTLoggingParams"] = (
            aws_sdk_iot.types.enable_io_t_logging_params.serialize_json(
                value["enable_io_t_logging_params"]
            )
        )
    if "publish_finding_to_sns_params" in value:
        import aws_sdk_iot.types.publish_finding_to_sns_params

        out["publishFindingToSnsParams"] = (
            aws_sdk_iot.types.publish_finding_to_sns_params.serialize_json(
                value["publish_finding_to_sns_params"]
            )
        )
    return out


def deserialize_json(data: dict) -> MitigationActionParams:
    out: MitigationActionParams = {}  # type: ignore[typeddict-item]
    if "updateDeviceCertificateParams" in data:
        import aws_sdk_iot.types.update_device_certificate_params

        out["update_device_certificate_params"] = (
            aws_sdk_iot.types.update_device_certificate_params.deserialize_json(
                data["updateDeviceCertificateParams"]
            )
        )
    if "updateCACertificateParams" in data:
        import aws_sdk_iot.types.update_ca_certificate_params

        out["update_ca_certificate_params"] = (
            aws_sdk_iot.types.update_ca_certificate_params.deserialize_json(
                data["updateCACertificateParams"]
            )
        )
    if "addThingsToThingGroupParams" in data:
        import aws_sdk_iot.types.add_things_to_thing_group_params

        out["add_things_to_thing_group_params"] = (
            aws_sdk_iot.types.add_things_to_thing_group_params.deserialize_json(
                data["addThingsToThingGroupParams"]
            )
        )
    if "replaceDefaultPolicyVersionParams" in data:
        import aws_sdk_iot.types.replace_default_policy_version_params

        out["replace_default_policy_version_params"] = (
            aws_sdk_iot.types.replace_default_policy_version_params.deserialize_json(
                data["replaceDefaultPolicyVersionParams"]
            )
        )
    if "enableIoTLoggingParams" in data:
        import aws_sdk_iot.types.enable_io_t_logging_params

        out["enable_io_t_logging_params"] = (
            aws_sdk_iot.types.enable_io_t_logging_params.deserialize_json(
                data["enableIoTLoggingParams"]
            )
        )
    if "publishFindingToSnsParams" in data:
        import aws_sdk_iot.types.publish_finding_to_sns_params

        out["publish_finding_to_sns_params"] = (
            aws_sdk_iot.types.publish_finding_to_sns_params.deserialize_json(
                data["publishFindingToSnsParams"]
            )
        )
    return out
