"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessInstanceLoggingConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.verified_access_instance_logging_configuration

VerifiedAccessInstanceLoggingConfigurationList: TypeAlias = list[
    "capo_ec2.types.verified_access_instance_logging_configuration.VerifiedAccessInstanceLoggingConfiguration"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessInstanceLoggingConfigurationList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.verified_access_instance_logging_configuration

        capo_ec2.types.verified_access_instance_logging_configuration.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    el: Element,
) -> VerifiedAccessInstanceLoggingConfigurationList:
    import capo_ec2.types.verified_access_instance_logging_configuration

    out: VerifiedAccessInstanceLoggingConfigurationList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.verified_access_instance_logging_configuration.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> VerifiedAccessInstanceLoggingConfigurationList:
    import capo_ec2.types.verified_access_instance_logging_configuration

    out: VerifiedAccessInstanceLoggingConfigurationList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.verified_access_instance_logging_configuration.deserialize_ec2_query(
                child
            )
        )
    return out
