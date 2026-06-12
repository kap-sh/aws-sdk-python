"""Generated from Smithy shape ``com.amazonaws.applicationinsights#Tier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_insights.errors import DeserializationError

Tier: TypeAlias = Literal[
    "CUSTOM",
    "DEFAULT",
    "DOT_NET_CORE",
    "DOT_NET_WORKER",
    "DOT_NET_WEB_TIER",
    "DOT_NET_WEB",
    "SQL_SERVER",
    "SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP",
    "MYSQL",
    "POSTGRESQL",
    "JAVA_JMX",
    "ORACLE",
    "SAP_HANA_MULTI_NODE",
    "SAP_HANA_SINGLE_NODE",
    "SAP_HANA_HIGH_AVAILABILITY",
    "SAP_ASE_SINGLE_NODE",
    "SAP_ASE_HIGH_AVAILABILITY",
    "SQL_SERVER_FAILOVER_CLUSTER_INSTANCE",
    "SHAREPOINT",
    "ACTIVE_DIRECTORY",
    "SAP_NETWEAVER_STANDARD",
    "SAP_NETWEAVER_DISTRIBUTED",
    "SAP_NETWEAVER_HIGH_AVAILABILITY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOM",
        "DEFAULT",
        "DOT_NET_CORE",
        "DOT_NET_WORKER",
        "DOT_NET_WEB_TIER",
        "DOT_NET_WEB",
        "SQL_SERVER",
        "SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP",
        "MYSQL",
        "POSTGRESQL",
        "JAVA_JMX",
        "ORACLE",
        "SAP_HANA_MULTI_NODE",
        "SAP_HANA_SINGLE_NODE",
        "SAP_HANA_HIGH_AVAILABILITY",
        "SAP_ASE_SINGLE_NODE",
        "SAP_ASE_HIGH_AVAILABILITY",
        "SQL_SERVER_FAILOVER_CLUSTER_INSTANCE",
        "SHAREPOINT",
        "ACTIVE_DIRECTORY",
        "SAP_NETWEAVER_STANDARD",
        "SAP_NETWEAVER_DISTRIBUTED",
        "SAP_NETWEAVER_HIGH_AVAILABILITY",
    )
)


def serialize_aws_json_1_1(value: Tier) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Tier:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Tier value: {data!r}")
    return cast(Tier, data)
