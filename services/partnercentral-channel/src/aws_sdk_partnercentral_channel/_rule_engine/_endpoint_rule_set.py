from __future__ import annotations

from typing import Any

from ._aws_partition import aws_partition
from ._endpoint_runtime import (
    Endpoint,
    EndpointError,
    get_attr,
    interpolate,
    string_equals,
)


class EndpointParams:
    def __init__(
        self,
        *,
        UseFIPS: bool | None = None,
        Endpoint: str | None = None,
        Region: str | None = None,
    ):
        self.UseFIPS = UseFIPS if UseFIPS is not None else False
        self.Endpoint = Endpoint if Endpoint is not None else None
        self.Region = Region if Region is not None else None


def resolve(p: EndpointParams) -> Endpoint:  # type: ignore
    """Resolve endpoint from parameters using generated ruleset."""
    _locals: dict[str, Any] = {}
    if p.Endpoint is not None:
        if p.UseFIPS is True:
            raise EndpointError(
                interpolate(
                    "Invalid Configuration: FIPS and custom endpoint are not supported",
                    p,
                    _locals,
                )
            )
        return Endpoint(
            url=p.Endpoint,
            properties={
                "authSchemes": [
                    {
                        "name": interpolate("sigv4a", p, _locals),
                        "signingRegionSet": [interpolate("*", p, _locals)],
                    },
                    {"name": interpolate("sigv4", p, _locals)},
                ]
            },
            headers={},
        )
    _locals: dict[str, Any] = {}
    if p.Region is not None:
        _locals["PartitionResult"] = aws_partition(p.Region)
        if _locals["PartitionResult"] is not None:
            if string_equals(
                get_attr(_locals["PartitionResult"], interpolate("name", p, _locals)),
                interpolate("aws-us-gov", p, _locals),
            ):
                if p.UseFIPS is False:
                    return Endpoint(
                        url=interpolate(
                            "https://partnercentral-channel.us-gov.{PartitionResult#dualStackDnsSuffix}",
                            p,
                            _locals,
                        ),
                        properties={
                            "authSchemes": [
                                {
                                    "name": interpolate("sigv4a", p, _locals),
                                    "signingRegionSet": [interpolate("*", p, _locals)],
                                },
                                {
                                    "name": interpolate("sigv4", p, _locals),
                                    "signingRegion": interpolate(
                                        "us-gov-west-1", p, _locals
                                    ),
                                },
                            ]
                        },
                        headers={},
                    )
            if string_equals(
                get_attr(_locals["PartitionResult"], interpolate("name", p, _locals)),
                interpolate("aws-us-gov", p, _locals),
            ):
                if p.UseFIPS is True:
                    return Endpoint(
                        url=interpolate(
                            "https://partnercentral-channel-fips.us-gov.{PartitionResult#dualStackDnsSuffix}",
                            p,
                            _locals,
                        ),
                        properties={
                            "authSchemes": [
                                {
                                    "name": interpolate("sigv4a", p, _locals),
                                    "signingRegionSet": [interpolate("*", p, _locals)],
                                },
                                {
                                    "name": interpolate("sigv4", p, _locals),
                                    "signingRegion": interpolate(
                                        "us-gov-west-1", p, _locals
                                    ),
                                },
                            ]
                        },
                        headers={},
                    )
            if p.UseFIPS is True:
                return Endpoint(
                    url=interpolate(
                        "https://partnercentral-channel-fips.global.{PartitionResult#dualStackDnsSuffix}",
                        p,
                        _locals,
                    ),
                    properties={
                        "authSchemes": [
                            {
                                "name": interpolate("sigv4a", p, _locals),
                                "signingRegionSet": [interpolate("*", p, _locals)],
                            },
                            {
                                "name": interpolate("sigv4", p, _locals),
                                "signingRegion": interpolate(
                                    "{PartitionResult#implicitGlobalRegion}", p, _locals
                                ),
                            },
                        ]
                    },
                    headers={},
                )
            return Endpoint(
                url=interpolate(
                    "https://partnercentral-channel.global.{PartitionResult#dualStackDnsSuffix}",
                    p,
                    _locals,
                ),
                properties={
                    "authSchemes": [
                        {
                            "name": interpolate("sigv4a", p, _locals),
                            "signingRegionSet": [interpolate("*", p, _locals)],
                        },
                        {
                            "name": interpolate("sigv4", p, _locals),
                            "signingRegion": interpolate(
                                "{PartitionResult#implicitGlobalRegion}", p, _locals
                            ),
                        },
                    ]
                },
                headers={},
            )
    raise EndpointError(
        interpolate("Invalid Configuration: Missing Region", p, _locals)
    )
    raise EndpointError("No endpoint rules matched")
