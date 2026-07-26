"""Generated from Smithy shape ``com.amazonaws.iot#TopicRuleDestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.http_url_destination_configuration
    import capo_iot.types.vpc_destination_configuration


class TopicRuleDestinationConfiguration(TypedDict, closed=True):
    http_url_configuration: NotRequired[
        "capo_iot.types.http_url_destination_configuration.HttpUrlDestinationConfiguration"
    ]
    """<p>Configuration of the HTTP URL.</p>"""
    vpc_configuration: NotRequired[
        "capo_iot.types.vpc_destination_configuration.VpcDestinationConfiguration"
    ]
    """<p>Configuration of the virtual private cloud (VPC) connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicRuleDestinationConfiguration) -> dict:
    out: dict = {}
    if "http_url_configuration" in value:
        import capo_iot.types.http_url_destination_configuration

        out["httpUrlConfiguration"] = (
            capo_iot.types.http_url_destination_configuration.serialize_json(
                value["http_url_configuration"]
            )
        )
    if "vpc_configuration" in value:
        import capo_iot.types.vpc_destination_configuration

        out["vpcConfiguration"] = (
            capo_iot.types.vpc_destination_configuration.serialize_json(
                value["vpc_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> TopicRuleDestinationConfiguration:
    out: TopicRuleDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if "httpUrlConfiguration" in data:
        import capo_iot.types.http_url_destination_configuration

        out["http_url_configuration"] = (
            capo_iot.types.http_url_destination_configuration.deserialize_json(
                data["httpUrlConfiguration"]
            )
        )
    if "vpcConfiguration" in data:
        import capo_iot.types.vpc_destination_configuration

        out["vpc_configuration"] = (
            capo_iot.types.vpc_destination_configuration.deserialize_json(
                data["vpcConfiguration"]
            )
        )
    return out
