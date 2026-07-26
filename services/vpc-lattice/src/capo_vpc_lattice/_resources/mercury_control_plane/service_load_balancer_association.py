from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from capo_vpc_lattice._services.async_vpc_lattice import (
        AsyncVPCLatticeClient,
    )
    from capo_vpc_lattice._services.vpc_lattice import (
        VPCLatticeClient,
    )


class ServiceLoadBalancerAssociation:
    def __init__(self, service: VPCLatticeClient) -> None:
        self._service = service


class AsyncServiceLoadBalancerAssociation:
    def __init__(self, service: AsyncVPCLatticeClient) -> None:
        self._service = service
